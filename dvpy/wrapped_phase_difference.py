import numpy as np
from .wrap_phase import wrap_phase

def wrapped_phase_difference(x, axis):
  return np.minimum(np.diff(x, 1, axis), np.diff(wrap_phase(x + np.pi), 1, axis))
