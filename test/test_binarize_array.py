import dvpy as dv
import numpy as np


def test_binarize_array():
    a = np.zeros((15, 15))
    a[0:10, 0:10] += 1
    a[5:15, 5:15] += 1
    assert np.sum(a) == 10 * 10 * 2

    dv.binarize_array(a)
    assert np.sum(a) == 10 * 10 * 2

    a = dv.binarize_array(a)
    assert np.sum(a) == 10 * 10 * 2 - 5 * 5
