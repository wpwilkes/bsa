"""
Test suite for the bucket sort algorithm.
"""

import unittest

import bsa


class TestBucketSort(unittest.TestCase):

    def test_bucket_sort(self):
        seq = [2, 3, 1]
        sorted_seq = bsa.bucket_sort(sequence=seq, inplace=False)
        seq.sort()
        self.assertTrue(sorted_seq == seq)


if __name__ == "__main__":
    unittest.main()
