import dvpy as dv
import numpy as np
from scipy.misc import face
import pylab as plt
import nibabel as nb


def test_random_transform_2d():

    img = face()

    x = dv.AugmentationParameters(
        image_dimension=2,
        translation_range=0.1,
        rotation_range=15,
        scale_range=0.1,
        flip=False,
        fill_mode="constant",
        cval=0.0,
    )

    txf = dv.generate_random_transform(x, img.shape)
    txf = dv.transform_full_matrix_offset_center(txf, img.shape[:-1])

    plt.imshow(dv.apply_affine_transform_channelwise(img, txf[:-1, :], channel_index=2))
    plt.show()


def test_random_transform_3d():

    a = np.sin(np.linspace(0, np.pi * 5, 256))
    b = np.cos(np.linspace(0, np.pi * 5, 256))
    img = np.outer(a, b)[..., np.newaxis] * a

    x = dv.AugmentationParameters(
        image_dimension=3,
        translation_range=0.15,
        rotation_range=45,
        scale_range=0.15,
        flip=False,
        fill_mode="constant",
        cval=0.0,
    )

    txf = dv.generate_random_transform(x, img.shape)
    txf = dv.transform_full_matrix_offset_center(txf, img.shape)

    nb.viewers.OrthoSlicer3D(dv.apply_affine_transform(img, txf[:-1, :])).show()
