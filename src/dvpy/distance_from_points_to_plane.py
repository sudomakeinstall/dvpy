import dvpy as dv
import numpy as np


def distance_from_points_to_plane(
    points, plane_origin=np.array([0, 0]), plane_normal=np.array([1, 0])
):
    return [
        [dv.distance_from_point_to_plane(p, plane_origin, plane_normal) for p in r]
        for r in points
    ]
