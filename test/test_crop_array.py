from dvpy import crop_array
import numpy as np


def test_crop_array():
    im = np.zeros((10, 10, 10))
    cr = crop_array(im, (2, 2, 2), (8, 8, 8))
    assert cr.shape == (8, 8, 8)

    im = np.matrix(np.zeros((10, 10)))
    cr = crop_array(im, (2, 2), (8, 8))
    assert cr.shape == (8, 8)
