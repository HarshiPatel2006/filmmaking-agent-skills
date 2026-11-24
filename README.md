# Filmmaking Agent Skills

**A portable, model- and agent-agnostic filmmaking knowledge library.** Use these skills to turn story intentions into cinematic decisions and reviewable production artifacts. The instructions are original operational syntheses of the five supplied filmmaking resources, with transparent source locators and limitations. This is version 0.1.0: source-informed, not exhaustively read or behaviorally benchmarked.

## Start here

- [Taxonomy](TAXONOMY.md) — 16 categories and their decision boundaries.
- [Skill tree](SKILL-TREE.md) — 62 independently usable `SKILL.md` entrypoints.
- [Agent protocol](AGENTS.md) — loading and handoff conventions.
- [Machine-readable registry](registry/skills.json) — descriptions, paths, inputs, outputs, sources and optional related skills.
- [Composite workflows](registry/workflows.json) — seven orchestrated procedures.
- [Sources](SOURCES.md), [coverage](knowledge/source-coverage.md), [overlap register](knowledge/knowledge-overlap-register.md), [gaps](knowledge/research-gaps.md).
- [Shared schemas](schemas/README.md), [evaluation cases](evaluations/README.md) and [rights](RIGHTS.md).

## Use with any agent

Point the agent at this repository or its extracted directory. Discover a suitable skill using the tree or JSON registry. Read only its `SKILL.md`; the `references/sources.md` is optional provenance. Each canonical skill works without other skills or external services. `agents/openai.yaml` supplies optional host UI metadata and is not needed for portability. Skill format follows the open [Agent Skills specification](https://agentskills.io/specification).

For a full scene, use [Direct a scene](workflows/direct-a-scene.md). For music-video production, use [Audio-led music video](workflows/audio-led-music-video.md). For an existing sequence, use [Continuity and quality review](workflows/continuity-and-quality-review.md). Keep platform-specific details in [adapters](adapters/README.md).

## Validate

Requires Python 3.10+ and PyYAML (only for repository validation, not for using skills). Run:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

Static validation checks structure and cross-references; it is not a film-quality benchmark.

## Publish your own repository

This package is prepared for GitHub but is not remotely published. After extracting it, create an empty **private** repository using your GitHub account. Run:

```sh
cd filmmaking-agent-skills
git init
git add .
git commit -m "Initial filmmaking skills library"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/filmmaking-agent-skills.git
git push -u origin main
```

Choose a license for original contributions and verify rights before changing visibility to public. The uploaded books are not included.
