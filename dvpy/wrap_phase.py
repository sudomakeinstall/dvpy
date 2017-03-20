import numpy as np

def wrap_phase(image):
  """ Wrap the input into the range [-pi, pi]."""
  return (image + np.pi) % (2.0 * np.pi) - np.pi
