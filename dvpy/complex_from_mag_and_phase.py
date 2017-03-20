import numpy as np

def complex_from_mag_and_phase(m, p):
  """
  Given magnitude and phase, create a complex number.

  Parameters
  ----------
  m : array-like
    Magnitude
  p : array-like (of same shape as m)
    Phase

  Returns
  -------
  c : array-like (of same shape as input)
    Elementwise complexified array

  """
  r = m * np.cos(p)
  i = m * np.sin(p)
  return r + i * 1.0j
