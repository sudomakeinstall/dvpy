import numpy as np

def crop_array(array, origin, dim):
  """
  Crop an array-like given origin and dimensions

  Parameters
  ----------
  array : array-like
    Array to be cropped.
  origin : tuple
    Indices of starting point to be cropped
  dim : tuple
    Dimensions to crop array to

  Returns
  -------
  out : array-like
    Cropped array
  """

  start = np.array(origin)
  end = start + np.array(dim)
  slices = [slice(s,e) for (s,e) in zip(start, end)]
  return array[slices]
  
