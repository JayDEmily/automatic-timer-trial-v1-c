import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])


    def test_trims_outer_whitespace(self):
        self.assertEqual(normalize(["  North ", "\twest\n", "East"]), ["North", "west", "East"])

    def test_omits_empty_and_whitespace_only_entries(self):
        self.assertEqual(normalize(["", " ", "\t\n", " x ", "", "  "]), ["x"])
        self.assertEqual(normalize(["", "\r\n", " "]), [])

    def test_preserves_order_and_duplicates_after_trimming(self):
        self.assertEqual(normalize([" a ", "B", "", "a", " B "]), ["a", "B", "a", "B"])

    def test_preserves_case_and_internal_whitespace_after_trimming(self):
        self.assertEqual(normalize(["  MiXeD  Case ", "\tC  d\t", " e\tf "]), ["MiXeD  Case", "C  d", "e\tf"])
