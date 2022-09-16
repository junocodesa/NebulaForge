"""Random project idea generator for NebulaForge."""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass
from typing import Iterable, List, Optional

DOMAINS = [
    "personal productivity",
    "decentralized finance",
    "content tooling",
    "AI-assisted learning",
    "research tooling",
    "experimental art",
    "community automation",
]

STACKS = {
    "web2": ["FastAPI", "Tailwind", "PostgreSQL", "GitHub Actions"],
    "web3": ["Foundry", "ethers.js", "The Graph", "IPFS"],
    "tool": ["Python CLI", "Click", "SQLite", "pydantic"],
    "ai": ["LangChain", "OpenAI", "gradio", "Redis"],
    "bot": ["Node.js", "Discord.py", "Cloud Functions", "Supabase"],
}

PERSPECTIVES = [
    "automatic journaling",
    "small-batch automation",
    "human-in-the-loop tutoring",
    "narrative-building for developers",
    "exploratory data-collecting",
]

DISCIPLINES = ["tooling", "spike", "utility", "automation", "experiment"]

PROJECT_ADJECTIVES = [
    "Quiet",
    "Curated",
    "Fragmented",
    "Polished",
    "Nebulous",
    "Orbiting",
    "Sonic",
]

ACTIONS = [
    "Sketch a lightweight UI mock",
    "Wire a data flow in a notebook",
    "Draft an API outline",
    "Record what went well this sprint",
    "Define the acceptance criteria",
]

MOTIVATIONS = [
    "bring clarity to a messy side project backlog",
    "turn a restless idea into one deliberate demo",
    "practice writing deeply human commit notes",
    "prove that a tiny tool can unlock a fresh habit",
    "balance new stack experiments with the busy week ahead",
]


@dataclass(frozen=True)
class ProjectIdea:
    name: str
    stack: List[str]
    domain: str
    perspective: str
    discipline: str
    story: str
    next_action: str
    motivation: str


class IdeaGenerator:
    def __init__(self, seed: Optional[int] = None) -> None:
        self.random = random.Random(seed)

    def pick_stack(self, focus: Optional[str]) -> List[str]:
        keys = list(STACKS.keys())
        if focus in STACKS:
            keys = [focus]
        chosen = self.random.choice(keys)
        palette = STACKS[chosen]
        custom = palette.copy()
        self.random.shuffle(custom)
        return custom[:3]

    def pick_domain(self) -> str:
        return self.random.choice(DOMAINS)

    def pick_perspective(self) -> str:
        return self.random.choice(PERSPECTIVES)

    def pick_discipline(self) -> str:
        return self.random.choice(DISCIPLINES)

    def make_name(self) -> str:
        adjective = self.random.choice(PROJECT_ADJECTIVES)
        suffix = self.pick_discipline().capitalize()
        timestamp = math.floor(self.random.random() * 9999)
        return f"{adjective} {suffix} {timestamp}"

    def describe(self, idea: ProjectIdea) -> str:
        return (
            f"Name: {idea.name}\n"
            f"Domain: {idea.domain}\n"
            f"Discipline: {idea.discipline}\n"
            f"Perspective: {idea.perspective}\n"
            f"Stack: {', '.join(idea.stack)}\n"
            f"Story: {idea.story}"
            f"\nNext action: {idea.next_action}"
            f"\nMotivation: {idea.motivation}"
        )

    def describe_detailed(self, idea: ProjectIdea) -> str:
        base = self.describe(idea)
        action_plan = self.make_action_plan(idea)
        return f"{base}\n\nAction plan:\n{action_plan}"

    def generate(self, focus: Optional[str] = None) -> ProjectIdea:
        stack = self.pick_stack(focus)
        domain = self.pick_domain()
        perspective = self.pick_perspective()
        discipline = self.pick_discipline()
        motivation = self.pick_motivation()
        story = (
            f"Build a {perspective} companion for {domain}, "
            f"incrementally delivering {discipline} helpers with {stack[0]} and friends {motivation}."
        )
        next_action = self.pick_next_action()
        return ProjectIdea(
            name=self.make_name(),
            stack=stack,
            domain=domain,
            perspective=perspective,
            discipline=discipline,
            story=story,
            next_action=next_action,
            motivation=motivation,
        )

    def pick_next_action(self) -> str:
        return self.random.choice(ACTIONS)

    def pick_motivation(self) -> str:
        return self.random.choice(MOTIVATIONS)

    def make_action_plan(self, idea: ProjectIdea) -> str:
        highlights = [
            f"- Sketch a {idea.stack[0]} prototype to prove the story",
            f"- Run a quick sanity check around {idea.domain} needs",
            f"- Capture why this matters: {idea.motivation}",
        ]
        return "\n".join(highlights)


def print_ideas(count: int, focus: Optional[str], seed: Optional[int], detail: bool) -> None:
    generator = IdeaGenerator(seed=seed)
    for index in range(1, count + 1):
        idea = generator.generate(focus)
        header = f"Idea {index}"
        print(header)
        print("-" * len(header))
        if detail:
            print(generator.describe_detailed(idea))
        else:
            print(generator.describe(idea))
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="nebulaforge",
        description="Spin up new solo project directions with a human-friendly story."
    )
    parser.add_argument("--count", "-c", type=int, default=1, help="how many ideas to show")
    parser.add_argument(
        "--focus",
        "-f",
        choices=list(STACKS.keys()),
        help="restrict the output to a particular stack category",
    )
    parser.add_argument("--seed", "-s", type=int, help="replay the same random stream")
    parser.add_argument(
        "--detail",
        action="store_true",
        help="print the action plan so each idea reads like a sprint recap",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print_ideas(count=args.count, focus=args.focus, seed=args.seed, detail=args.detail)


if __name__ == "__main__":
    main()
