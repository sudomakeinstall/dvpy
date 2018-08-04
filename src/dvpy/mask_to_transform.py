# System

# Third Party
import numpy as np
import scipy.ndimage.interpolation as itp
from scipy.ndimage.measurements import center_of_mass

# Internal
import dvpy as dv


def mask_to_transform(seg, rotation=0.0, margin=0.0, radians=True, return_images=False):

    assert seg.ndim == 2

    seg_original = seg.copy()
    seg = dv.binarize_array(seg)

    ##
    ## Calculate Useful Quantities
    ##

    ctr = [s // 2 for s in seg.shape]
    com = center_of_mass(seg)
    nrm = [
        2.0 * (i_com - i_ctr) / i_shp
        for i_com, i_ctr, i_shp in zip(com, ctr, seg.shape)
    ]
    ost = [-n * c for n, c in zip(nrm, ctr)]

    if radians:
        rotation = np.degrees(rotation)

    ##
    ## Translation
    ##

    seg_xy = itp.shift(seg, ost, order=0, mode="constant", cval=0)

    ##
    ## Rotation
    ##

    seg_rt = itp.rotate(seg_xy, rotation, reshape=False, order=0, mode="nearest")

    ##
    ## Zoom
    ##

    bbox = dv.bounding_box(seg_rt)

    scale = [(i_max - i_min) / i_shp for (i_min, i_max), i_shp in zip(bbox, seg.shape)]

    scale = max(scale)

    scale = min(1.0, scale + margin * 2.0)

    if return_images:
        seg_xy = itp.shift(seg_original, ost, order=0, mode="constant", cval=0)
        seg_rt = itp.rotate(seg_xy, rotation, reshape=False, order=0, mode="nearest")
        seg_zm = dv.crop_or_pad(itp.zoom(seg_rt, 1.0 / scale, order=0), seg.shape)
        return nrm, -np.radians(rotation), scale, seg_xy, seg_rt, seg_zm
    else:
        return nrm, -np.radians(rotation), scale
