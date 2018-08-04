import dvpy as dv
import numpy as np


def test_fit_plane():

    center = np.array([[5, 0, -100]]).transpose()
    scale = np.array([100.0, 100.0, 1.0])

    pts = np.random.randn(3, 10000)  # Random point cloud.
    pts = np.diag(scale).dot(pts)  # Scaled
    pts = pts + center  # Translated

    c, n = dv.fit_plane(pts)  # Center, Normal
