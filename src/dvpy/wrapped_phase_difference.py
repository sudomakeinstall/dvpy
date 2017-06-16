import numpy as np
from .wrap_phase import wrap_phase

def wrapped_phase_difference(x, ax):
  padding = [[0, 0] for _ in range(2)]
  padding[ax][1] = 1
  x1 = np.pad(np.diff(x,                     n = 1, axis = ax), padding, 'edge')
  x2 = np.pad(np.diff(wrap_phase(x + np.pi), n = 1, axis = ax), padding, 'edge')
  return np.minimum(x1, x2)
