import numpy as np

def complex_from_mag_and_phase(m, p):
  r = m * np.cos(p)
  i = m * np.sin(p)
  return r + i * 1.0j
