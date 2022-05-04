"""
Test suite for the bubble sort algorithm.
"""

import unittest

import bsa


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        bsa.bubble_sort([2, 3, 1])


if __name__ == "__main__":
    unittest.main()
