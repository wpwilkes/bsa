"""
Implementation of insertion sort.
"""

from typing import Optional
import copy

from bsa.utils import ComparableSequence
import bsa.utils as utils


def insertion_sort(sequence: ComparableSequence,
                   inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the insertion sort algorithm.

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
        _insertion_sort(sequence)
        return
    return _insertion_sort(copy.copy(sequence))


def _insertion_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the insertion sort algorithm.
    """
    N = len(sequence)
    for i in range(1, N):
        j = i
        while j > 0 and sequence[j-1] > sequence[j]:
            utils.swap(sequence, j, j-1)
            j -= 1
    return sequence
