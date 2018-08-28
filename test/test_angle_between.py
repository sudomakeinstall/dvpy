import dvpy as dv
import numpy as np


def test_angle_between():
    assert np.allclose(0, dv.angle_between([1, 0], [1, 0]))
    assert np.allclose(np.pi / 4, dv.angle_between([1, 1], [1, 0]))
    assert np.allclose(np.pi / 2, dv.angle_between([0, 1], [1, 0]))
    assert np.allclose(3 * np.pi / 4, dv.angle_between([-1, 1], [1, 0]))
    assert np.allclose(np.pi, dv.angle_between([-1, 0], [1, 0]))
