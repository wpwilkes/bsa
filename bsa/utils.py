"""
Implementation of various utilities.
"""

from abc import ABCMeta, abstractmethod
from typing import Any, MutableSequence, TypeVar


class _Comparable(metaclass=ABCMeta):

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        pass


Comparable = TypeVar("Comparable", bound=_Comparable)


ComparableSequence = MutableSequence[Comparable]


def swap(sequence: ComparableSequence, i: int, j: int) -> None:
    """
    Swap the elements of `sequence` at indices `i` and `j`.
    """
    sequence[i], sequence[j] = sequence[j], sequence[i]
