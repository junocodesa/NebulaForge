"""Simple checks to keep the generator behaving like a human journaler."""

import unittest

from nebulaforge.idea_generator import IdeaGenerator


class IdeaGeneratorTests(unittest.TestCase):
    def test_generate_is_repeatable_with_seed(self) -> None:
        first_run = IdeaGenerator(seed=42).generate()
        second_run = IdeaGenerator(seed=42).generate()
        self.assertEqual(first_run, second_run)

    def test_action_plan_tracks_stack_and_motivation(self) -> None:
        generator = IdeaGenerator(seed=99)
        idea = generator.generate()
        plan = generator.make_action_plan(idea)
        self.assertIn(idea.stack[0], plan)
        self.assertIn(idea.domain, plan)
        self.assertIn(idea.motivation, plan)


if __name__ == "__main__":
    unittest.main()
