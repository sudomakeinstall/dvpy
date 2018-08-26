import numpy as np

import dvpy as dv

def project_point_onto_line(o, v, p):
    r"""
    Project a point `p` onto a plane defined by a point `o` and vector `v`.

    The vector projection of one vector onto another, where these two vectors are understood
    to share an origin, is given by `dvpy.vector_projection`.  However, it is frequently the
    case that the point `p` is given with respect to the origin, and that the vector `v` is
    given with respect to a distinct origin, `o`.  In this case, it is necessary that `o` be
    subtracted from `p` prior to calculating the vector projection, and that it be added back
    prior to returning.

    .. plot::

        import numpy as np
        import pylab as plt
        import dvpy as dv

        o = np.array([2.0, 2.0])
        v = np.array([2.0, 1.0])
        p = np.array([2.5, 3.0])

        x = dv.project_point_onto_line(o, v, p)

        line = np.array([o, o + v]).transpose()

        size = 100

        plt.plot(line[0], line[1], '--')

        plt.scatter(*o, s = size, c = 'red')
        plt.scatter(*(o + v), s = size, c = 'orange')
        plt.scatter(*p, s = size, c = 'green')
        plt.scatter(*x, s = size, c = 'blue')

        plt.axis('equal')
        plt.show()

    :param o: Origin of the plane.
    :type o: Array-like.

    :param v: Normal of the plane.
    :type v: Array-like, of length equal to `o`.

    :param p: Point to be projected onto the plane.
    :type p: Array-like, of length equal to `o`.

    :returns: The projection of `p` projected onto the plane.
    :rtype: Array-like, of length equal to `o`.

    """
    return o + dv.vector_projection(p - o, v)

