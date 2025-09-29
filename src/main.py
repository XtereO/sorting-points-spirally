from math import atan2, acos, sin, cos
from typing import List
import matplotlib.pyplot as plt

from utils import pop_by_value


def sort_points_spirally(points: List[List[float]], showing_result=False) -> List[int]:
    """Algorithm sorts a list of points in spiral order.

    Args:
        points (list of lists): A list of (x, y, z) coordinates (must be at least 2 dimensions).

    Returns:
        list of indexes: Indexes of sorted points in spiral order.
    """

    if (len(points) == 0):
        return []

    indexed_points = list(enumerate(points))
    pivot_point = pop_by_value(indexed_points, min(
        indexed_points, key=lambda ip: (ip[1][0], ip[1][1], ip[1][2])))

    res = [pivot_point]

    while indexed_points:
        pivot_point = points[res[-1]]
        pivot_x, pivot_y, pivot_z = pivot_point

        x_min = min([*indexed_points, (res[-1], pivot_point)],
                    key=lambda ip: (ip[1][0], ip[1][1], ip[1][2]))[1][0]
        x_max = max([*indexed_points, (res[-1], pivot_point)],
                    key=lambda ip: (ip[1][0], ip[1][1], ip[1][2]))[1][0]
        y_min = min([*indexed_points, (res[-1], pivot_point)],
                    key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))[1][1]
        y_max = max([*indexed_points, (res[-1], pivot_point)],
                    key=lambda ip: (ip[1][1], ip[1][0], ip[1][2]))[1][1]
        y_mean = y_min + ((y_max-y_min)/2)
        x_mean = x_min + ((x_max-x_min)/2)

        shifted_pivot_x = pivot_x - x_mean
        shifted_pivot_y = pivot_y - y_mean
        unsigned_alpha = 0 if shifted_pivot_x == 0 else acos(
            (-shifted_pivot_x) / ((shifted_pivot_x**2 + shifted_pivot_y**2)**0.5))
        alpha = -unsigned_alpha if (shifted_pivot_y < 0) else unsigned_alpha
        s = sin(alpha)
        c = cos(alpha)

        angles = sorted([{"angle": (atan2(c*(p[0]-pivot_x) + s*(pivot_y-p[1]), c*(p[1]-pivot_y)+s*(p[0]-pivot_x))), "index": i}
                        for i, p in (indexed_points)], key=lambda a: (round(a["angle"], 4), (points[a["index"]][0]*s + points[a["index"]][1]*c), (points[a["index"]][0]*c - points[a["index"]][1]*s), points[angles["index"]][2]),
                        reverse=False)

        next_pivot_point_index = angles[0]["index"]
        pop_by_value(indexed_points, (next_pivot_point_index,
                     points[next_pivot_point_index]))
        res.append(next_pivot_point_index)

    if (showing_result):
        x_ordered = list(map(lambda i: points[i][0], res))
        y_ordered = list(map(lambda i: points[i][1], res))
        plt.plot(x_ordered, y_ordered, marker='o')
        plt.show()

    return res
