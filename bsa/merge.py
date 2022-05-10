"""
Implementation of merge sort.
"""


def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array
    mid = len(array) // 2
    L = array[:mid]
    R = array[mid:]
    return _merge(merge_sort(L), merge_sort(R))


def _merge(L, R):
    A = L + R
    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    return A
