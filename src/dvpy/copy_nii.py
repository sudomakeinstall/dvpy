# System

# Third Party
import nibabel as nb
import numpy as np

# Internal


def copy_nii(image, return_components=False):
    d = image.get_data().copy()
    a = image.affine.copy()
    h = image.header.copy()
    if return_components:
        return d, a, h
    else:
        return nb.Nifti1Image(d, a, header=h)
