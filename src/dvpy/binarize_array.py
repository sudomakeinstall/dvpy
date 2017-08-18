import numpy as np

def binarize_array(x):
  r = x.copy()
  r[r != 0] = 1
  return r
