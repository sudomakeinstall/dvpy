import numpy as np


def distance_from_point_to_plane(
    point, plane_origin=np.array([0, 0]), plane_normal=np.array([1, 0])
):
    point_n = point - plane_origin
    plane_n = plane_normal - plane_origin
    return np.dot(point_n, plane_n) / la.norm(plane_n)
