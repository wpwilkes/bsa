"""
Implementation of bubble sort.
"""

from typing import Optional
import copy

from bsa.utils import ComparableSequence
import bsa.utils as utils


def bubble_sort(sequence: ComparableSequence,
                inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the bubble sort algorithm.

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
        _bubble_sort(sequence)
        return
    return _bubble_sort(copy.copy(sequence))


def _bubble_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the bubble sort algorithm.
    """
    N = len(sequence)
    for num_sorted in range(N):
        swapped = False
        for current in range(N - num_sorted - 1):
            next = current + 1
            unsorted = sequence[current] > sequence[next]
            if unsorted:
                utils.swap(sequence, next, current)
                swapped = True
        if not swapped:
            break
    return sequence
