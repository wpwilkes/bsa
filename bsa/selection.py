"""
"""

from typing import Optional

from .utils import swap


def selection_sort(array: list, asc=True, inplace=True) -> Optional[list]:
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
        swap(array, i, midx)

    if not inplace:
        return array