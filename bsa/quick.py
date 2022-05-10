"""
Implementation of quick sort.
"""

import random


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    pivot = array[random.randrange(0, len(array))]
    L = [i for i in array if i < pivot]
    E = [i for i in array if i == pivot]
    R = [i for i in array if i > pivot]
    return quick_sort(L) + E + quick_sort(R)
