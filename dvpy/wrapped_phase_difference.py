import numpy as np
import unwrap as uw
from .wrap_phase import wrap_phase

def wrapped_phase_difference(x, ax):
#  x1 = np.diff(x, 1, axis)
#  x2 = np.diff(wrap_phase(x + np.pi), 1, axis)
  x = uw.unwrap(x)
  x1 = np.gradient(x,                     axis = ax)
  x2 = np.gradient(wrap_phase(x + np.pi), axis = ax)
  out = x1
  out[np.real(x) >= 0] = x2[np.real(x) >= 0]

  return out
