import numpy as np
from .wrap_phase import wrap_phase

def wrapped_phase_difference(x, axis):
  x1 = np.diff(x, 1, axis)
  x2 = np.diff(wrap_phase(x + np.pi), 1, axis)
  out = x1
  out[np.real(x) >= 0] = x2[np.real(x) >= 0]

  return out
