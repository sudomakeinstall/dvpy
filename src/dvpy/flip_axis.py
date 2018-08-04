# System

# Third Party
import numpy as np

# Internal


def flip_axis(array, axis):
    """
    Flip the given axis of an array.  Note that the ordering follows the
    numpy convention and may be unintuitive; that is, the first axis
    flips the axis horizontally, and the second axis flips the axis vertically.

    :param array: The array to be flipped.
    :type array: `ndarray`

    :param axis: The axis to be flipped.
    :type axis: `int`

    :returns: The flipped array.
    :rtype: `ndarray`
    """

    # Rearrange the array so that the axis of interest is first.
    array = np.asarray(array).swapaxes(axis, 0)
    # Reverse the elements along the first axis.
    array = array[::-1, ...]
    # Put the array back and return.
    return array.swapaxes(0, axis)
