#!/usr/bin/env sh
# Run NebulaForge the way I would after finishing the day job.
# The detail flag keeps the output ready for a commit message.
python nebulaforge/idea_generator.py --count 2 --detail "$@"
