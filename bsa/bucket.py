"""
Implementation of bucket sort.
"""

from typing import MutableSequence, Optional
import copy


def bucket_sort(sequence: MutableSequence[int],
                inplace: bool = True) -> Optional[MutableSequence[int]]:
    """
    Sort the sequence using the bucket sort algorithm.

    Parameters
    ----------
    sequence : MutableSequence[int]
        The sequence of integers to sort.
    inplace : bool, optional
        Whether to sort inplace (True) or not (False). Default is
        `True`.

    Returns
    -------
    union[MutableSequence[int], None] :
        If inplace, then `None` is returned. Otherwise, the sorted
        sequence is returned.
    """
    if inplace:
        _bucket_sort(sequence)
        return
    return _bucket_sort(copy.copy(sequence))


def _bucket_sort(sequence: MutableSequence[int]) -> MutableSequence[int]:
    """
    Sort the sequence using the bucket sort algorithm.
    """
    N = max(sequence)
    buckets = []
    for index in range(N+1):
        buckets.append([])
    for value in sequence:
        buckets[value].append(value)
    sequence = []
    for index in range(N+1):
        bucket = buckets[index]
        for value in bucket:
            sequence.append(value)
    return sequence
