"""
Implementation of insertion sort.
"""

from typing import Optional

import bsa.utils as utils


def insertion_sort(array: list, inplace=True) -> Optional[list]:
    """
    """
    if not inplace:
        array = array.copy()

    N = len(array)
    for i in range(1, N):
        j = i
        while j > 0 and array[j-1] > array[j]:
            utils.swap(array, j, j-1)
            j -= 1

    if not inplace:
        return array
