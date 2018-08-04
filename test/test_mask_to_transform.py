import dvpy as dv
import numpy as np
import pylab as plt


def test_mask_to_transform():
    a = np.zeros((800, 1600))
    a[0:400, 0:800] = 1

    xy, rt, zm, xy_i, rt_i, zm_i = dv.mask_to_transform(
        a, rotation=np.pi / 8, return_images=True
    )
