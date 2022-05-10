"""
Implementation of quick sort.
"""

from typing import Optional
import copy
import random

from bsa.utils import ComparableSequence


def quick_sort(sequence: ComparableSequence,
               inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the quick sort algorithm.

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
        _quick_sort(sequence)
        return
    return _quick_sort(copy.copy(sequence))


def _quick_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the quick sort algorithm.
    """
    n = len(sequence)
    if n < 2:
        return sequence
    pivot = sequence[random.randrange(0, n)]
    L = [i for i in sequence if i < pivot]
    E = [i for i in sequence if i == pivot]
    G = [i for i in sequence if i > pivot]
    return _quick_sort(L) + E + _quick_sort(G)
