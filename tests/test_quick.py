"""
Test suite for the quick sort algorithm.
"""

import unittest

import bsa


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.quick_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
