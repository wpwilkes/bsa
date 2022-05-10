"""
Test suite for the bubble sort algorithm.
"""

import unittest

import bsa


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.bubble_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
