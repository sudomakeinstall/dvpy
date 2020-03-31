import dvpy as dv
import nibabel as nb
import numpy as np


def test_convert_nii():
    data = np.random.randint(low=0, high=101, size=(5, 5, 5))
    im = nb.Nifti1Image(data, np.eye(4))
    for rescale in [True, False]:
        for dtype in ["uint8", "int8", "uint16", "int16"]:
            dv.convert_nii(im, dtype, rescale=rescale)
