# System

# Third Party
import numpy as np

# Internal


def crop_or_pad(array, target, value=0):
    """
    Symmetrically pad or crop along each dimension to the specified target dimension.

    :param array: Array to be cropped / padded.
    :type array: array-like

    :param target: Target dimension.
    :type target: `int` or array-like of length array.ndim

    :returns: Cropped/padded array. 
    :rtype: array-like
    """
    # Pad each axis to at least the target.
    margin = target - np.array(array.shape)
    padding = [(0, max(x, 0)) for x in margin]
    array = np.pad(array, padding, mode="constant", constant_values=value)
    for i, x in enumerate(margin):
        array = np.roll(array, shift=+(x // 2), axis=i)

    if type(target) == int:
        target = [target] * array.ndim

    ind = tuple([slice(0, t) for t in target])
    return array[ind]
