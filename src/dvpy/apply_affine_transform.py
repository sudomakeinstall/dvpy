import numpy as np
from scipy.ndimage.interpolation import affine_transform

def apply_affine_transform(array,
      transform_matrix,
      channel_index=0,
      fill_mode='constant',
      cval=0.,
      order=0):
    """
    Apply an affine transform to an image.

    :param array: Array to be transformed.
    :type array: 3-dimensional `ndarray`

    :param transform_matrix: Transformation matrix.
    :type array: `ndarray`

    :param channel_index: Axis corresponding to the RGB channel.
    :type channel_index: `int`

    :param fill_mode: How to pad image; default is 'constant.'
    :type fill_mode: `str`

    :param cval: Used when fill mode is constant.
    :type cval: `scalar`

    :param order: The order of spline interpolation.
    :type order: `int`

    :returns: Transformed version of input matrix.
    :rtype: `ndarray`

    :raises: `ValueError` if image dimensions or matrix shape are incorrect.
    """
    # 
    if array.ndim != 3:
      raise ValueError('Input array must have 3 dimensions.')

    array = np.rollaxis(array, channel_index, 0)
    final_affine_matrix = transform_matrix[:2, :2] 
    final_offset = transform_matrix[:2, 2]
    array = [affine_transform(x_channel,
               final_affine_matrix,
               final_offset,
               order=0,
               mode=fill_mode,
               cval=cval) for x_channel in array]
    array = np.stack(array, axis=0)
    return np.rollaxis(array, 0, channel_index+1)

