"""
Test suite for the selection sort algorithm.
"""

import unittest

import bsa


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.selection_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
