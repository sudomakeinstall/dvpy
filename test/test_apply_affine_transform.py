import dvpy as dv
import numpy as np
import pytest as pt
from scipy.misc import face
import pylab as plt

def test_apply_affine_transform():
  I = np.array([[1, 0, 0], [0, 1, 0]])

  test = face()
  translate = np.array([[1, 0, test.shape[0]//2], [0, 1, test.shape[1]//2]])
  plt.imshow(dv.apply_affine_transform(test, translate, channel_index=2))
  plt.show()
