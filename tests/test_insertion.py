"""
Test suite for the insertion sort algorithm.
"""

import unittest

import bsa


class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.insertion_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
