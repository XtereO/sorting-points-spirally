from typing import List
import matplotlib.pyplot as plt


def sort_points_spirally(points: List[List[float]], showing_result=False) -> List[int]:
    """Algorithm sorts a list of points in spiral order.

    Args:
        points (list of lists): A list of (x, y, z) coordinates (must be at least 2 dimensions).

    Returns:
        list of indexes: Indexes of sorted points in spiral order.
    """

    if (len(points) == 0):
        return []

    pivot_point = points.index(min(points, key=lambda p: (p[0], p[1], p[2])))

    res = [pivot_point]

    if (showing_result):
        x_ordered = list(map(lambda i: points[i][0], res))
        y_ordered = list(map(lambda i: points[i][1], res))
        plt.plot(x_ordered, y_ordered, marker='o')
        plt.show()

    return res
