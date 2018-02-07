import dvpy as dv
import numpy as np

def test_jaccard_index():

  t = np.ones((2, 2)) * 5
  p = np.ones((2, 2)) * 5

  assert(np.allclose(dv.jaccard_index(t, p, 5), 1.00))
  p[0,0] = 1
  assert(np.allclose(dv.jaccard_index(t, p, 5), 0.75))
  p[0,1] = 2
  assert(np.allclose(dv.jaccard_index(t, p, 5), 0.50))
  p[1,0] = 3
  assert(np.allclose(dv.jaccard_index(t, p, 5), 0.25))
  p[1,1] = 4
  assert(np.allclose(dv.jaccard_index(t, p, 5), 0.00))
