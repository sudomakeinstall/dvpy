# System

# Third Party
import numpy as np
from scipy.ndimage.interpolation import affine_transform

# Internal


def apply_affine_transform_channelwise(
    array, transform_matrix, channel_index=0, fill_mode="constant", cval=0., order=0
):
    """
    Apply an affine transform to an image.

    :param array: Array to be transformed.
    :type array: n-dimensional `ndarray`

    :param transform_matrix: Transformation matrix, in homogeneous coordinates.
    :type array: 2-dimensional `ndarray`

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

    array = np.rollaxis(array, channel_index, 0)
    array = [
        apply_affine_transform(
            x_channel, transform_matrix, fill_mode=fill_mode, cval=cval, order=0
        )
        for x_channel in array
    ]
    array = np.stack(array, axis=0)
    return np.rollaxis(array, 0, channel_index + 1)


def apply_affine_transform(
    array, transform_matrix, fill_mode="constant", cval=0., order=0
):
    """
    Apply an affine transform to an image.

    :param array: Array to be transformed.
    :type array: n-dimensional `ndarray`

    :param transform_matrix: Transformation matrix, in homogeneous coordinates.
    :type array: 2-dimensional `ndarray`

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
    # Check dimensions
    if transform_matrix.ndim != 2:
        raise ValueError("The transformation matrix must have 2 dimensions.")

    if transform_matrix.shape[0] != array.ndim:
        raise ValueError(
            "The first dimension of the transformation matrix must be equal to array.ndim."
        )

    if transform_matrix.shape[1] != array.ndim + 1:
        raise ValueError(
            "The second dimension of the transformation matrix must be equal to array.ndim + 1."
        )

    final_affine_matrix = transform_matrix[: array.ndim, : array.ndim]
    final_offset = transform_matrix[: array.ndim, array.ndim]

    return affine_transform(
        array, final_affine_matrix, final_offset, order=0, mode=fill_mode, cval=cval
    )
