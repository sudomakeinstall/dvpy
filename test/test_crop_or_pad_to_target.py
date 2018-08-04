
import numpy as np
import dvpy as dv


def test_crop_or_pad():

    ##
    ## Test when a target is an `int`
    ##

    # a.ndim == 1
    a = np.ones((75))
    t = dv.crop_or_pad(a, 64)
    assert np.allclose(t.shape, [64])

    a = np.ones((75))
    t = dv.crop_or_pad(a, 128)
    assert np.allclose(t.shape, [128])

    # a.ndim == 2
    a = np.ones((75, 75))
    t = dv.crop_or_pad(a, 64)
    assert np.allclose(t.shape, [64, 64])

    a = np.ones((75, 75))
    t = dv.crop_or_pad(a, 128)
    assert np.allclose(t.shape, [128, 128])

    # a.ndim == 3
    a = np.ones((75, 75, 75))
    t = dv.crop_or_pad(a, 64)
    assert np.allclose(t.shape, [64, 64, 64])

    a = np.ones((75, 75, 75))
    t = dv.crop_or_pad(a, 128)
    assert np.allclose(t.shape, [128, 128, 128])

    ##
    ## Test when a target is an `int`
    ##

    # a.ndim == 1
    a = np.ones((75))
    t = dv.crop_or_pad(a, (64))
    assert np.allclose(t.shape, [64])

    a = np.ones((75))
    t = dv.crop_or_pad(a, (128))
    assert np.allclose(t.shape, [128])

    # a.ndim == 2
    a = np.ones((75, 75))
    t = dv.crop_or_pad(a, (64, 64))
    assert np.allclose(t.shape, [64, 64])

    a = np.ones((75, 75))
    t = dv.crop_or_pad(a, (128, 128))
    assert np.allclose(t.shape, [128, 128])

    # a.ndim == 3
    a = np.ones((75, 75, 75))
    t = dv.crop_or_pad(a, (64, 64, 64))
    assert np.allclose(t.shape, [64, 64, 64])

    a = np.ones((75, 75, 75))
    t = dv.crop_or_pad(a, (128, 128, 128))
    assert np.allclose(t.shape, [128, 128, 128])
