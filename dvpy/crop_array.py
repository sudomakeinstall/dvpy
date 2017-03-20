import numpy as np

def crop_array(array, origin, dim):

  start = np.array(origin)
  end = start + np.array(dim)
  slices = [slice(s,e) for (s,e) in zip(start, end)]
  return array[slices]
  
