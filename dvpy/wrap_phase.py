import numpy as np

def wrap_phase(x):
  """
  Wrap the input into the range [-pi, pi].

  Parameters
  ----------
  x: array-like
    Number, array, or matrix to be phase wrapped.

  Returns
  -------
  output: array-like
    A structure of the same shape as the input wrapped
    into the range [-pi, pi] elementwise.

  """
  return (x + np.pi) % (2.0 * np.pi) - np.pi
