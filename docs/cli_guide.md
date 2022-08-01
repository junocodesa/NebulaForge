# CLI Reference for Luminous Atlas

`python nebulaforge/idea_generator.py` powers the CLI that keeps Luminous Atlas moving. Every run prints a short narrative plus, optionally, a tiny action plan so that the history stays practical.

- `--count, -c <n>`: run the generator `n` times in one go so the open loop stays active.
- `--focus, -f <category>`: pin the output to one of the stack grooves (`web2`, `web3`, `tool`, `ai`, `bot`).
- `--seed, -s <number>`: replay a stream; handy when a particular idea deserves a follow-up commit.
- `--detail`: add an explicit action plan below each idea so this tool reads like a sprint review.

Use the `--detail` flag whenever you want to drop a mini checklist right into your next commit message.
