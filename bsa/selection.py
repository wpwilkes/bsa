"""
Implementation of selection sort.
"""

from typing import Optional

import bsa.utils as utils


def selection_sort(array: list, inplace=True) -> Optional[list]:
    """
    """
    if not inplace:
        array = array.copy()

    N = len(array)
    for i in range(N):
        midx = i
        for j in range(i+1, N):
            if array[midx] > array[j]:
                midx = j
        utils.swap(array, i, midx)

    if not inplace:
        return array