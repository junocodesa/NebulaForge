# NebulaForge Idea Studio

NebulaForge is the living lab for *Luminous Atlas*, the personal project playbook I write solo after the day job. The generator spins up random but plausible feature sets, stacks, and narratives so I can iterate on intimate, believable slices of a project. Each run becomes a mini sprint: pick a direction, sketch a story, and commit just the right amount of code.

## What It Does

- crafts ideas covering web2, web3, tooling, AI, analytics, learning, and research angles
- mixes responsibilities (data client, automation bot, command-line helper, lightweight API, etc.) with matching stacks
- keeps the narrative personal: add drama to the constraints and next action items so each commit feels human
- lets me iterate in short bursts so that the working history looks like a journaling of a real solo dev

## Structure

- `docs/project_manifest.md`: captures what Luminous Atlas is trying to do and why each commit matters
- `nebulaforge/idea_generator.py`: spins up ideas with a CLI to bake in tone and output formats
- `README.md`: explains the goals, how to run the generator, and what to do once an idea feels solid

## Next Moves

1. Run `python nebulaforge/idea_generator.py --count 3` to inspect possible project directions for today.
2. Copy the generated idea into a journal entry (`notes/day-...`) and sketch the first small PR-worthy slice.
3. Code, commit, and re-run the tool each time for inspiration before drafting the next change.
4. Once everything feels finished, bundle the notes into a post and celebrate the solo project.

## Running

```bash
python nebulaforge/idea_generator.py --count 2 --focus ai
```

No dependencies beyond the standard library; this is intentionally lightweight so it can stay in the repo forever without rewriting history.
