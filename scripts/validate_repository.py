#!/usr/bin/env python3
"""Check the portable repository structure; not a behavioral benchmark."""
from pathlib import Path
import argparse, json, re, sys, csv
import yaml
ROOT=Path(__file__).resolve().parents[1]

def validate(root):
    errors=[]
    def require(condition,message):
        if not condition: errors.append(message)
    def load(path):
        try: return json.loads((root/path).read_text(encoding='utf8'))
        except Exception as exc: errors.append(f'{path}: {exc}'); return None
    for p in root.rglob('*.json'):
        load(p.relative_to(root))
    registry=load('registry/skills.json') or []
    categories=load('registry/categories.json') or []
    deps=load('registry/dependencies.json') or {}
    workflows=load('registry/workflows.json') or []
    tests=load('evaluations/test-cases.json') or []
    manifest=load('knowledge/source-manifest.json') or []
    ids=[r.get('id') for r in registry]; idset=set(ids)
    cats={c.get('id'):c for c in categories}; sourcepages={s['source']:s['local_pdf_pages'] for s in manifest}
    require(len(ids)==len(idset),'duplicate registry ID')
    require(len(cats)==len(categories),'duplicate category ID')
    paths={r.get('path') for r in registry}
    actual={p.relative_to(root).as_posix() for p in (root/'skills').glob('*/SKILL.md')}
    require(paths==actual,'registry paths differ from on-disk skills')
    for r in registry:
        name=r.get('id',''); path=root/r.get('path',''); tag=f'{name}: '
        require(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name)) and len(name)<=64,tag+'invalid ID')
        require(r.get('category') in cats,tag+'missing category')
        require(path.parent.name==name,tag+'directory/name mismatch')
        require(r.get('inputs') and r.get('outputs'),tag+'missing input/output')
        require(bool(r.get('sources')),tag+'missing source locators')
        for src in r.get('sources',[]):
            code=src.get('source'); require(code in sourcepages,tag+'unknown source '+str(code))
            for interval in src.get('pdf_pages','').split(','):
                try:
                    a,*rest=map(int,interval.split('-')); b=rest[0] if rest else a
                    require(1<=a<=b<=sourcepages.get(code,0),tag+'invalid source page '+str(interval))
                except Exception: errors.append(tag+'unparseable page range '+interval)
        for ref in r.get('related_skills',[])+r.get('prerequisites',[]):
            require(ref in idset and ref!=name,tag+'invalid skill reference '+ref)
        if not path.is_file(): continue
        text=path.read_text(encoding='utf8'); m=re.match(r'^---\n(.*?)\n---\n(.*)$',text,re.S)
        require(m is not None,tag+'missing YAML frontmatter')
        if not m: continue
        try: fm=yaml.safe_load(m.group(1))
        except Exception as exc: errors.append(tag+str(exc)); continue
        require(isinstance(fm,dict) and set(fm)=={'name','description'},tag+'invalid frontmatter keys')
        if not isinstance(fm,dict): continue
        require(fm.get('name')==name,tag+'name mismatch')
        desc=fm.get('description'); require(isinstance(desc,str) and 1<=len(desc)<=1024 and desc==r.get('description'),tag+'description mismatch')
        body=m.group(2)
        require(len(body.split())>=130 and len(text.splitlines())<500,tag+'body size outside policy')
        for sec in ('Inputs and deliverable','Decision procedure','Diagnose and correct','Output checks','Practice case'):
            require('## '+sec in body,tag+'missing '+sec)
        require(not re.search(r'\bTODO\b|\[FILL IN\]|\[YOUR .*?\]',body),tag+'placeholder')
        require((path.parent/'references/sources.md').is_file(),tag+'missing source notes')
        require((path.parent/'agents/openai.yaml').is_file(),tag+'missing optional host metadata')
    for c in categories:
        require(c['skill_count']==sum(r.get('category')==c['id'] for r in registry),'wrong category count: '+c['id'])
    edges=deps.get('mandatory_edges',[]); graph={x:[] for x in idset}
    for e in edges:
        a,b=e['from'],e['to']; require(a in idset and b in idset,'missing mandatory endpoint')
        if a in graph and b in graph: graph[a].append(b)
    active=set(); finished=set()
    def visit(x):
        if x in active: errors.append('mandatory dependency cycle at '+x); return
        if x in finished:return
        active.add(x)
        for y in graph[x]:visit(y)
        active.remove(x);finished.add(x)
    for x in graph:visit(x)
    expected={(r['id'],s) for r in registry for s in r.get('related_skills',[])}
    actual_edges={(e['from'],e['to']) for e in deps.get('related_edges',[])}
    require(expected==actual_edges,'related graph mismatch')
    for w in workflows:
        require((root/w['path']).is_file(),'workflow file missing: '+w['id'])
        require(all(s in idset for s in w['skills']),'workflow skill missing: '+w['id'])
    require(len(tests)==len(ids) and {t['skill'] for t in tests}==idset,'missing or duplicate evaluation cases')
    for t in tests:
        require(t.get('input') and t.get('expected_deliverable') and t.get('acceptance_criteria'),'incomplete test '+t['id'])
    for p in root.rglob('*.md'):
        s=p.read_text(encoding='utf8')
        for link in re.findall(r'\]\(([^)]+)\)',s):
            if link.startswith(('http://','https://','mailto:','#')):continue
            target=link.split('#')[0]
            if target: require((p.parent/target).exists(),f'broken link {p.relative_to(root)} -> {link}')
    for p in root.rglob('*'):
        if p.is_file(): require(p.suffix.lower() not in {'.pdf','.mp4','.jpg','.png'},f'unexpected source/media asset {p.relative_to(root)}')
    with (root/'knowledge/source-coverage.csv').open(encoding='utf8') as f:
        for row in csv.DictReader(f):
            require(row['source'] in sourcepages,'unknown coverage source')
            require(all(s in idset for s in row['skill_ids'].split(',')),'missing coverage skill in '+row['topic'])
    return errors,{'skills':len(ids),'categories':len(cats),'workflows':len(workflows),'behavioral_cases':len(tests),'related_edges':len(expected),'schemas':len(list((root/'schemas').glob('*.schema.json')))}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT); args=p.parse_args()
    errors,counts=validate(args.root)
    print(json.dumps({'status':'FAIL' if errors else 'PASS','counts':counts,'errors':errors},indent=2))
    sys.exit(bool(errors))
