import numpy as np

import dvpy as dv


def project_point_onto_line(o, v, p):
    r"""
    Project a point `p` onto a line defined by a point `o` and vector `v`.

    The vector projection of one vector onto another, where these two vectors are understood
    to share an origin, is given by `dvpy.vector_projection`.  However, it is frequently the
    case that the point `p` is given with respect to the origin, and that the vector `v` is
    given with respect to a distinct origin, `o`.  In this case, it is necessary that `o` be
    subtracted from `p` prior to calculating the vector projection, and that it be added back
    prior to returning.

    .. plot:: plots/project_point_onto_line.py

    :param o: Origin of the line.
    :type o: Array-like.

    :param v: Vector parallel to the line.
    :type v: Array-like, of length equal to `o`.

    :param p: Point to be projected onto the line.
    :type p: Array-like, of length equal to `o`.

    :returns: The projection of `p` onto the line.
    :rtype: Array-like, of length equal to `o`.

    """
    return o + dv.vector_projection(p - o, v)
