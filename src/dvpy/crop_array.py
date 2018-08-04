# System

# Third Party
import numpy as np

# Internal


def crop_array(array, origin, dim):
    """
  Crop an array-like given origin and dimensions

  :param array: Array to be cropped.
  :type array: array-like

  :param origin: Indices of starting point to be cropped
  :type origin: tuple

  :param dim: Dimensions to crop array to
  :type dim: tuple

  :returns: Cropped array
  :rtype: array-like
  """

    start = np.array(origin)
    end = start + np.array(dim)
    slices = [slice(s, e) for (s, e) in zip(start, end)]
    return array[slices]
