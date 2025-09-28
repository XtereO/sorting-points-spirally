from typing import List, TypeVar

T = TypeVar("T")


def pop_by_value(lst: List[T], value: T) -> int:
    try:
        index = lst.index(value)
        lst.pop(index)
        return index
    except ValueError:
        return -1
