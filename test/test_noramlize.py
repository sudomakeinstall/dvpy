import dvpy as dv
import numpy as np

data = [([1, 0], [5, 0]), ([0, 1], [0, 5]), ([-1, 0], [-5, 0]), ([0, -1], [0, -5])]


def test_normalize():
    for u, v in data:
        assert np.allclose(u, dv.normalize(v))
