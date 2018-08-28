# System

# Third Party
import numpy as np

# Internal


def normalize(v):
    r"""
    Given a vector `v`, return the corresponding unit vector (same direction, unit magnitude).

    .. math::
        \hat{v} = \frac{v}{\|v\|}

    Where:

    .. math::
        \|v\| = \sqrt{ v \cdot v }

    :param v: The vector to be normalized.
    :type v: An array-like with dimension 1.

    :returns: The unit vector corresponding to `v`.
    :rtype: An array-like with the same shape as `v`.
    """

    return v / np.linalg.norm(v)
