import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trim_edges(self):
        self.assertEqual(normalize(["  North ", "\tWest\n", " east"]), ["North", "West", "east"])

    def test_omit_empty_after_trim(self):
        self.assertEqual(normalize(["", " ", "\t\n", "x", "  "]), ["x"])

    def test_trim_preserves_order_and_duplicates(self):
        self.assertEqual(normalize([" B ", "a", "B", "  a  "]), ["B", "a", "B", "a"])

    def test_trim_preserves_case_and_internal_whitespace(self):
        self.assertEqual(normalize(["  Ab  C\tD  ", " e F "]), ["Ab  C\tD", "e F"])
