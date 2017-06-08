import numpy as np

def wrapped_phase_difference(x, axis):
  return np.minimum(np.diff(x, 1, axis), np.diff(dv.wrap_phase(x + np.pi), 1, axis))
