import re
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from helpers import generate_flag  # noqa: E402


class GenerateFlagTest(unittest.TestCase):
    def test_flag_matches_default_auditfarm_format(self):
        flag = generate_flag()

        self.assertRegex(flag, re.compile(r'^[A-Z0-9]{31}=$'))

    def test_flags_are_random(self):
        self.assertNotEqual(generate_flag(), generate_flag())


if __name__ == '__main__':
    unittest.main()
