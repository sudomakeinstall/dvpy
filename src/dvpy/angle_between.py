import numpy as np
import dvpy as dv


def angle_between(v1, v2):
    r"""
    Returns the angle in radians between vectors :math:`v_1` and :math:`v_2`.

    The definition of the dot product [1] is as follows (where :math:`\theta` is the angle between :math:`v_1` and :math:`v_2`):

    .. math::
        v_1 \cdot v_2 = \| v_1 \| \| v_2 \| \cos(\theta)

    The equation is simplified if the vectors are first normalized:

    .. math::
        \hat{v_1} \cdot \hat{v_2} = \cos(\theta)

    We now solve for :math:`\theta`:

    .. math::
        \theta = \cos^{-1} ( \hat{v_1} \cdot \hat{v_2} )

    Lastly, to avoid numerical errors, it is necessary to clip the dot product to the range :math:`[-1, 1]`:

    .. math::
        \theta = \cos^{-1} ( \max( \min( \hat{v_1} \cdot \hat{v_2}, +1), -1) )

    :param v1: The first vector.
    :type v1: An array-like.

    :param v2: The second vector.
    :type v2: An array-like, with the same length as `v1`.

    [1] https://en.wikipedia.org/wiki/Dot_product#Geometric_definition
    """
    v1_u = dv.normalize(v1)
    v2_u = dv.normalize(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
