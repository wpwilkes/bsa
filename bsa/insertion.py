"""
"""

from typing import Optional

from .utils import swap


def insertion_sort(array: list, asc=True, inplace=True) -> Optional[list]:
    """
    """
    if not inplace:
        array = array.copy()

    N = len(array)
    for i in range(1, N):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array, j, j-1)
            j -= 1

    if not inplace:
        return array
