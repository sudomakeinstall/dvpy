import dvpy as dv
import numpy as np


def test_fit_plane_to_points():

    coefs_gt = [1.0, 2.0, 3.0, 4.0]
    coefs_gt = coefs_gt / np.linalg.norm(coefs_gt)
    xx, yy = np.meshgrid(np.linspace(-50, +50, 100), np.linspace(-75, +25, 100))
    zz = (-coefs_gt[0] * xx - coefs_gt[1] * yy - coefs_gt[3]) / coefs_gt[2]

    xx = xx.flatten()
    yy = yy.flatten()
    zz = zz.flatten()

    points = np.array([xx, yy, zz]).transpose()

    coefs = dv.fit_plane_to_points(points)
    coefs = coefs / np.linalg.norm(coefs)
