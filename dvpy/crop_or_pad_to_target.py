import numpy as np

def crop_or_pad_to_target(array, target):
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

