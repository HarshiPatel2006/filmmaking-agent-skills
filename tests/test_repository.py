import json, shutil, tempfile, unittest, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_repository import validate

class ValidationTests(unittest.TestCase):
    def test_complete_repository(self):
        errors, counts=validate(ROOT)
        self.assertEqual(errors,[])
        self.assertEqual(counts['skills'],62)
    def mutate(self, action, phrase):
        with tempfile.TemporaryDirectory() as tmp:
            dst=Path(tmp)/'repo'; shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('.git','__pycache__'))
            action(dst)
            errors,_=validate(dst)
            self.assertTrue(any(phrase in e for e in errors),errors)
    def test_missing_entrypoint(self):
        self.mutate(lambda p:(p/'skills/premise-and-logline/SKILL.md').unlink(),'paths differ')
    def test_bad_skill_name(self):
        def bad(p):
            f=p/'skills/premise-and-logline/SKILL.md'; f.write_text(f.read_text().replace('name: premise-and-logline','name: WRONG'))
        self.mutate(bad,'name mismatch')
    def test_bad_reference(self):
        def bad(p):
            f=p/'registry/skills.json'; data=json.loads(f.read_text());data[0]['related_skills'].append('nonexistent');f.write_text(json.dumps(data))
        self.mutate(bad,'invalid skill reference')
    def test_dependency_cycle(self):
        def bad(p):
            f=p/'registry/dependencies.json';d=json.loads(f.read_text());d['mandatory_edges']=[{'from':'premise-and-logline','to':'theme-and-motif'},{'from':'theme-and-motif','to':'premise-and-logline'}];f.write_text(json.dumps(d))
        self.mutate(bad,'mandatory dependency cycle')
    def test_invalid_source_page(self):
        def bad(p):
            f=p/'registry/skills.json';d=json.loads(f.read_text());d[0]['sources'][0]['pdf_pages']='9999';f.write_text(json.dumps(d))
        self.mutate(bad,'invalid source page')

if __name__=='__main__':unittest.main()
