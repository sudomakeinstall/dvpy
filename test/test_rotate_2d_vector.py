
import dvpy as dv
import numpy as np


def test_rotate_2d_vector():
    vec = np.array([1, 0])
    assert np.allclose(dv.rotate_2d_vector(vec, np.pi / 2.0), [0, +1])
    assert np.allclose(dv.rotate_2d_vector(vec, np.pi), [-1, 0])
    assert np.allclose(dv.rotate_2d_vector(vec, 3.0 * np.pi / 2.0), [0, -1])
