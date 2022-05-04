"""
Implementation of bubble sort.
"""

from typing import Optional

import bsa.utils as utils



def bubble_sort(array: list,
                asc=True,
                inplace=True) -> Optional[list]:
    """
    """
    if not inplace:
        array = array.copy()

    N = len(array)
    for num_sorted in range(N):
        swapped = False
        for current in range(N - num_sorted - 1):
            next = current + 1
            if asc:
                unsorted = array[current] > array[next]
            else:
                unsorted = array[current] < array[next]
            if unsorted:
                utils.swap(array, next, current)
                swapped = True
        if not swapped:
            break

    if not inplace:
        return array
