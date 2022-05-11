"""
Test suite for the heap sort algorithm.
"""

import unittest

import bsa


class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.heap_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
