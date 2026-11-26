import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trim_surrounding_whitespace(self):
        self.assertEqual(normalize(["  North ", "\twest\n"]), ["North", "west"])

    def test_omit_blank_entries(self):
        self.assertEqual(normalize(["", " \t\n", " keep ", "", "\r\n"]), ["keep"])
        self.assertEqual(normalize(["", " ", "\t"]), [])

    def test_trim_preserves_order_duplicates_case_and_internal_whitespace(self):
        self.assertEqual(normalize([" North ", " west", "North\t", " C  d ", "a\tb "]),
                         ["North", "west", "North", "C  d", "a\tb"])
