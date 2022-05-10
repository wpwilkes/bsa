"""
Implementation of selection sort.
"""

from typing import Optional
import copy

from bsa.utils import ComparableSequence
import bsa.utils as utils


def selection_sort(sequence: ComparableSequence,
                   inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the selection sort algorithm.

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
        _selection_sort(sequence)
        return
    return _selection_sort(copy.copy(sequence))


def _selection_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the selection sort algorithm.
    """
    n = len(sequence)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if sequence[min_idx] > sequence[j]:
                min_idx = j
        if i != min_idx:
            utils.swap(sequence, i, min_idx)
    return sequence
