"""
Implementation of merge sort.
"""

from typing import Optional
import copy

from bsa.utils import ComparableSequence


def merge_sort(sequence: ComparableSequence,
               inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the merge sort algorithm.

    Parameters
    ----------
    sequence : ComparableSequence
        The sequence of comparable objects to sort.
    inplace : bool, optional
        Whether to sort inplace (True) or not (False). Default is
        `True`.

    Returns
    -------
    union[ComparableSequence, None] :
        If inplace, then `None` is returned. Otherwise, the sorted
        sequence is returned.
    """
    if inplace:
        _merge_sort(sequence)
        return
    return _merge_sort(copy.copy(sequence))


def _merge_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the merge sort algorithm.
    """
    n = len(sequence)
    if n < 2:
        return sequence
    mid = n // 2
    s1 = sequence[:mid]
    s2 = sequence[mid:]
    return _merge(_merge_sort(s1), _merge_sort(s2))


def _merge(s1: ComparableSequence,
           s2: ComparableSequence) -> ComparableSequence:
    """
    Merge two sorted sequences into one sorted sequence.
    """
    n1, n2 = len(s1), len(s2)
    s = s1 + s2
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if s1[i] < s2[j]:
            s[k] = s1[i]
            i += 1
        else:
            s[k] = s2[j]
            j += 1
        k += 1
    while i < n1:
        s[k] = s1[i]
        i += 1
        k += 1
    while j < n2:
        s[k] = s2[j]
        j += 1
        k += 1
    return s
