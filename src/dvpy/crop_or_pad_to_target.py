import numpy as np

def crop_or_pad(array, target):
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
    padding = [(0,max(x,0)) for x in margin]
    array = np.pad(array,
                   padding,
                   mode='constant',
                   constant_values=0)
    for i, x in enumerate(margin):
        array = np.roll(array, shift = +(x//2), axis = i)

    if type(target) == int:
      target = [target] * array.ndim

    ind = [slice(0, t) for t in target]
    return array[ind]

def crop_or_pad_to_target(array, target):
    assert(False)
    """
    Symmetrically pad or crop along each dimension to the specified target dimension.
    """
    # Pad each axis to at least the target.
    x = target - array.shape[0]
    y = target - array.shape[1]
    padding = [(0,max(x,0)),(0,max(y,0))]
    if array.ndim == 3: padding.append((0,0))
    array = np.pad(array,
                   padding,
                   mode='constant',
                   constant_values=0)
    # Now center it
    array = np.roll(array, shift = +(x//2), axis = 0)
    array = np.roll(array, shift = +(y//2), axis = 1)
    ind = [slice(0,target),slice(0,target)]
    if array.ndim == 3: ind.append(slice(None))
    return array[ind]

