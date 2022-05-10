"""
Test suite for the merge sort algorithm.
"""

import unittest

import bsa


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.merge_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
