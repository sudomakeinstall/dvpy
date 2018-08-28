
import numpy as np


def vector_projection(v1, v2):
    r"""
    The vector projection [1] of `v_1` onto `v_2`.  Note that `v_1` and `v_2` are
    understood to share an origin.

    .. math::
        \frac{v_1 \cdot v_2}{v_2 \cdot v_2} v_2
        

    [1] https://en.wikipedia.org/wiki/Vector_projection#Vector_projection_2
    """

    return np.dot(v1, v2) / np.dot(v2, v2) * v2
