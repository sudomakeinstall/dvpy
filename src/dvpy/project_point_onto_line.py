import numpy as np

def project_point_onto_line(o, v, p):
    """
    Project a point `p` onto a plane defined by a point `o` and vector `v`.

    :param o: Origin of the plane.
    :type o: Vector length 3.

    :param v: Normal of the plane.
    :type v: Vector length 3.

    :param p: Point to be projected onto the plane.
    :type p: Vector length 3.

    :returns: The projection of `p` projected onto the plane.
    :rtype: Vector length 3.
    """
    return o + np.dot(p - o, v) / np.dot(v, v) * v

