import dvpy as dv
import numpy as np


def project_point_onto_plane(o, n, p):
    r"""
    Project a point `p` onto a plane defined by a point `o` and normal `n`.

    .. plot:: plots/project_point_onto_plane.py

    :param o: Origin of the plane.
    :type o: Array-like length 3.

    :param n: Normal of the plane.
    :type n: Array-like length 3.

    :param p: Point to be projected onto the plane.
    :type p: Array-like length 3.

    :returns: The projection of `p` projected onto the plane.
    :rtype: Array-like length 3.

    """
    n_u = dv.normalize(n)
    return p - np.dot(p - o, n_u) * n_u
