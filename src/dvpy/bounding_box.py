# System

# Third Party
import numpy as np

# Internal
import dvpy as dv


def bounding_box(array):
    """ 
    Get the bounding box from an `ndarray`.

    :param array: The input array.
    :type array: ndarray

    :returns: A list of tuples.  `len(out) == array.ndim`; the tuples have length two and specify the first and last index in that dimension containing a value which evaluates to `True`.
    :rtype: [(int, int), ...]

    :raises: `ValueError` if all values are near zero.
    """

    if np.allclose(array, np.zeros(array.shape)):
        raise ValueError("The bounding box of an all-zero array is ambiguous.")

    # A special condition is necessary for ndim == 1 because np.any()
    # behaves differently for a one-dimensional array as opposed to
    # higher dimensional arrays.
    if array.ndim == 1:
        return [tuple(np.where(array == True)[0][[0, -1]])]
        raise ValueError("Currently only multidimensional arrays are supported.")

    # Now deal with higher dimensional arrays
    all_indices = list(range(array.ndim))
    any_all = [
        np.any(array, axis=tuple(dv.pop_and_return(all_indices, n)))
        for n in range(array.ndim)
    ]
    return [tuple(np.where(x)[0][[0, -1]]) for x in any_all]
