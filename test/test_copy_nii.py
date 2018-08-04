import dvpy as dv
import nibabel as nb
import numpy as np


def test_copy_nii():
    image = nb.Nifti1Image(np.ones((5, 5, 5)), np.eye(4))

    # Try returning components
    d, a, h = dv.copy_nii(image, return_components=True)

    assert d is not image.get_data()
    assert a is not image.affine
    assert h is not image.header

    # Try returning new image
    new_image = dv.copy_nii(image, return_components=False)

    assert new_image.get_data() is not image.get_data()
    assert new_image.affine is not image.affine
    assert new_image.header is not image.header
