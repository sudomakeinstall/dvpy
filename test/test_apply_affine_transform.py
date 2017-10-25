import dvpy as dv
import numpy as np
import pytest as pt
from scipy.misc import ascent, face
import pylab as plt

def test_apply_affine_transform():
  ##
  ## 2D (Grayscale)
  ##

  test = ascent()
  I = np.array([[1, 0, 0], [0, 1, 0]])
  S = np.array([[2, 0, 0], [0, 2, 0]])
  T = np.array([[1, 0, test.shape[0]//2],
                [0, 1, test.shape[1]//2]])

  plt.imshow(dv.apply_affine_transform(test, dv.transform_partial_matrix_offset_center(I, test.shape)))
  plt.show()

  plt.imshow(dv.apply_affine_transform(test, dv.transform_partial_matrix_offset_center(S, test.shape)))
  plt.show()

  plt.imshow(dv.apply_affine_transform(test, dv.transform_partial_matrix_offset_center(T, test.shape)))
  plt.show()

  ##
  ## 2D (Color)
  ##

  test = face()
  T = np.array([[1, 0, test.shape[0]//2],
                [0, 1, test.shape[1]//2]])

  plt.imshow(dv.apply_affine_transform_channelwise(test, I, channel_index = 2))
  plt.show()

  plt.imshow(dv.apply_affine_transform_channelwise(test, S, channel_index = 2))
  plt.show()

  plt.imshow(dv.apply_affine_transform_channelwise(test, T, channel_index = 2))
  plt.show()

