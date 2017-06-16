import numpy as np

def helper_pop_and_return(l, n):
  o = l.copy()
  del o[n]
  return o

def bounding_box(array):
  """ 
  Get the bounding box from an ndarray

  Parameters
  ----------
  array: array-like
    An array-like object

  Returns
  -------
  output: A list of tuples
    The length of the list matches the number of dimensions of the input array.
    The tuples each have length two.  The first and second elements of each
    tuple represent the first and last index in that dimension containing a
    value which evaluates to True.
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
  any_all = [np.any(array, axis = tuple(helper_pop_and_return(all_indices, n))) for n in range(array.ndim)]
  return [tuple(np.where(x)[0][[0, -1]]) for x in any_all]

