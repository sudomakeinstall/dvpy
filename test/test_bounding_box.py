import numpy as np
import pytest as pt
import dvpy as dv


def test_bounding_box():
    # An array with all zeros is ambiguous
    with pt.raises(ValueError) as err:
        dv.bounding_box(np.zeros((5, 5)))

    # Make sure it works at various dimensions
    x = np.ones((5))
    assert np.allclose(dv.bounding_box(x), [(0, 4)])

    x = np.ones((5, 5))
    assert np.allclose(dv.bounding_box(x), [(0, 4), (0, 4)])

    x = np.ones((5, 5, 5))
    assert np.allclose(dv.bounding_box(x), [(0, 4), (0, 4), (0, 4)])

    #
    x = np.zeros((5, 5))
    x[0, 0] = 1
    assert np.allclose(dv.bounding_box(x), [(0, 0), (0, 0)])

    x = np.zeros((5, 5))
    x[0, 0] = 1
    x[4, 4] = 1
    assert np.allclose(dv.bounding_box(x), [(0, 4), (0, 4)])

    x = np.zeros((5, 5))
    x[1:3, 2:4] = 1
    assert np.allclose(dv.bounding_box(x), [(1, 2), (2, 3)])
