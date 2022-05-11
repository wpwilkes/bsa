"""
Implementation of heap sort.
"""

from typing import Optional
import copy

from bsa.utils import ComparableSequence
import bsa.utils as utils


def heap_sort(sequence: ComparableSequence,
              inplace: bool = True) -> Optional[ComparableSequence]:
    """
    Sort the sequence using the heap sort algorithm.

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
        _heap_sort(sequence)
        return
    return _heap_sort(copy.copy(sequence))


def _heap_sort(sequence: ComparableSequence) -> ComparableSequence:
    """
    Sort the sequence using the heap sort algorithm.
    """
    n = len(sequence)
    for i in range(n//2 - 1, -1, -1):
        _heapify(sequence, i, n - 1)
    for i in range(n - 1, -1 , -1):
        utils.swap(sequence, 0, i)
        _heapify(sequence, 0, i - 1)
    return sequence


def _heapify(sequence: ComparableSequence,
             root_idx: int,
             last_idx: int) -> None:
    """
    Heapify the given sequence.
    """
    max_idx = root_idx
    lc_idx = 2 * root_idx + 1
    rc_idx = 2 * root_idx + 2
    if lc_idx <= last_idx:
        if sequence[lc_idx] > sequence[root_idx]:
            max_idx = lc_idx
    if rc_idx <= last_idx:
        if sequence[rc_idx] > sequence[max_idx]:
            max_idx = rc_idx
    if root_idx != max_idx:
        utils.swap(sequence, root_idx, max_idx)
        _heapify(sequence, max_idx, last_idx)
