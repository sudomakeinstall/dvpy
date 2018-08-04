# System

# Third Party
import numpy as np
import pytest as pt
from scipy.misc import ascent, face
import pylab as plt
import nibabel as nb

# Internal
import dvpy as dv


def test_apply_affine_transform():
    ##
    ## 2D (Grayscale)
    ##

    test = ascent()
    I = np.array([[1, 0, 0], [0, 1, 0]])
    S = np.array([[2, 0, 0], [0, 2, 0]])
    F = np.array([[-1, 0, 0], [0, 1, 0]])
    T = np.array([[1, 0, test.shape[0] // 2], [0, 1, test.shape[1] // 2]])

    for t in [I, S, F, T]:
        plt.imshow(
            dv.apply_affine_transform(
                test, dv.transform_partial_matrix_offset_center(t, test.shape)
            )
        )
        plt.show()

    ##
    ## 2D (Color)
    ##

    test = face()
    T = np.array([[1, 0, test.shape[0] // 2], [0, 1, test.shape[1] // 2]])

    for t in [I, S, F, T]:
        plt.imshow(
            dv.apply_affine_transform_channelwise(
                test,
                dv.transform_partial_matrix_offset_center(t, test.shape[:-1]),
                channel_index=2,
            )
        )
        plt.show()

    ##
    ## 3D (Grayscale)
    ##

    a = np.sin(np.linspace(0, np.pi, 21))
    b = np.cos(np.linspace(0, np.pi * 5, 21))
    test = np.outer(a, b)[..., np.newaxis] * a

    I = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    S = np.array([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0]])
    F = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    T = np.array(
        [
            [1, 0, 0, test.shape[0] // 2],
            [0, 1, 0, test.shape[1] // 2],
            [0, 0, 1, test.shape[2] // 2],
        ]
    )

    for t in [I, S, F, T]:
        a = np.sin(np.linspace(0, np.pi, 20))
        b = np.cos(np.linspace(0, np.pi * 5, 20))
        test = np.outer(a, b)[..., np.newaxis] * a
        nb.viewers.OrthoSlicer3D(
            dv.apply_affine_transform(
                test, dv.transform_partial_matrix_offset_center(t, test.shape)
            )
        ).show()
