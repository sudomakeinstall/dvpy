# System

# Third Party
import nibabel as nb
import numpy as np
import skimage.exposure as ex

# Internal
import dvpy as dv


def convert_nii(im, new_dtype, rescale=False):
    d, a, h = dv.copy_nii(im, return_components=True)
    if rescale:
        d = np.nan_to_num(d)
        d = ex.rescale_intensity(d, in_range="image", out_range=new_dtype)
    else:
        d = d.astype(new_dtype)

    new_image = nb.Nifti1Image(d, a, header=h)
    new_image.set_data_dtype(new_dtype)

    return new_image
