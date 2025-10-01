from math import acos, sin, cos, atan2
from typing import List, Tuple, TypeVar


def pick_next_point_rotated_atan2(points: List[List[float]], indexed_points: List[Tuple], pivot_point: Tuple[float]) -> int:
    shifted_pivot_x, shifted_pivot_y, pivot_x, pivot_y = pivot_point

    unsigned_alpha = 0 if shifted_pivot_x == 0 else acos(
        (-shifted_pivot_x) / ((shifted_pivot_x**2 + shifted_pivot_y**2)**0.5))
    alpha = -unsigned_alpha if (shifted_pivot_y < 0) else unsigned_alpha
    s = sin(alpha)
    c = cos(alpha)

    indexed_angles = sorted([{"angle": round(atan2(c*(p[0]-pivot_x) + s*(pivot_y-p[1]), c*(p[1]-pivot_y)+s*(p[0]-pivot_x)), 4), "index": i}
                             for i, p in indexed_points],
                            key=lambda ia: (ia["angle"], (points[ia["index"]][0]*s + points[ia["index"]][1]*c),
                                            (points[ia["index"]][0]*c - points[ia["index"]][1]*s), points[ia["index"]][2]),
                            reverse=False)

    next_pivot_point_index = indexed_angles[0]["index"]
    for ia in indexed_angles:
        next_pivot_point_index = ia["index"]
        if ia["angle"] >= -1.5708:
            break

    return next_pivot_point_index


def pick_next_point_shifted_scalar_product(points: List[List[float]], indexed_points: List[Tuple], pivot_point: Tuple[float]) -> int:
    shifted_pivot_x, shifted_pivot_y, pivot_x, pivot_y = pivot_point
    x_mean, y_mean = pivot_x - shifted_pivot_x, pivot_y - shifted_pivot_y

    indexed_angles = sorted([{"angle": (1 if (-shifted_pivot_y*(p[0]-x_mean) + shifted_pivot_x*(p[1]-y_mean)) >= 0 else -1) *
                              acos((-pivot_x*(p[0]-pivot_x)-pivot_y*(p[1]-pivot_y))/((pivot_x**2+pivot_y**2)**0.5 * ((p[0]-pivot_x)**2+(p[1]-pivot_y)**2)**0.5)), "index": i} for i, p in indexed_points],
                            key=lambda ia: (
                                ia["angle"], points[ia["index"]][0], points[ia["index"]][1], points[ia["index"]][2]),
                            reverse=False)

    return indexed_angles[0]["index"]


pick_next_point = {
    "rotated_atan2": pick_next_point_rotated_atan2,
    "scalar_product": pick_next_point_shifted_scalar_product
}
