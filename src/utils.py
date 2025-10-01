from typing import List, Tuple, TypeVar


def get_boundaries_indexed_points(indexed_points: List[Tuple]) -> Tuple[float]:
    if not indexed_points or len(indexed_points) == 1:
        return (0, 0, 0, 0)

    x_min = min(indexed_points,
                key=lambda ip: (ip[1][0], ip[1][1], ip[1][2]))[1][0]
    x_max = max(indexed_points,
                key=lambda ip: (ip[1][0], ip[1][1], ip[1][2]))[1][0]
    y_min = min(indexed_points,
                key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))[1][1]
    y_max = max(indexed_points,
                key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))[1][1]

    return (x_min, x_max, y_min, y_max)

T = TypeVar("T")
def pop_by_value(lst: List[T], value: T) -> int:
    try:
        index = lst.index(value)
        lst.pop(index)
        return index
    except ValueError:
        return -1
