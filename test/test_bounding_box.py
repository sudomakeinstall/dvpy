import numpy as np
import pytest as pt
from dvpy.bounding_box import *

def test_bounding_box():
  with pt.raises(ValueError) as err:
    bounding_box(np.zeros((5, 5)))

  x = np.ones((5))
  assert(np.allclose(bounding_box(x), [(0, 4)]))

  x = np.ones((5, 5))
  assert(np.allclose(bounding_box(x), [(0, 4), (0, 4)]))

  x = np.ones((5, 5, 5))
  assert(np.allclose(bounding_box(x), [(0, 4), (0, 4), (0, 4)]))

  x = np.zeros((5, 5))
  x[0,0] = 1
  assert(np.allclose(bounding_box(x), [(0, 0), (0, 0)]))

  x = np.zeros((5, 5))
  x[1:3, 2:4] = 1
  assert(np.allclose(bounding_box(x), [(1, 2), (2, 3)]))

