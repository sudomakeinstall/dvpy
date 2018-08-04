# System

# Third Party
import numpy as np

# Internal


def subdivide_quadratic_bspline(points):

    (r, c) = points.shape
    out = np.zeros((2 * r, c), dtype=np.float64)

    for i1 in range(r):
        i2 = (i1 + 1) % r

        p1 = points[i1, :] * 0.75 + points[i2, :] * 0.25
        p2 = points[i1, :] * 0.25 + points[i2, :] * 0.75

        out[i1 * 2, :] = p1
        out[i1 * 2 + 1, :] = p2

    return out
