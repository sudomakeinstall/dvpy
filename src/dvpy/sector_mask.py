# System

# Third Party
import numpy as np

# Internal

# https://stackoverflow.com/questions/18352973/mask-a-circular-sector-in-a-numpy-array#41743189
def sector_mask(shape, centre, radius, angle_range=(0, np.pi * 2), degrees=False):
    """
    Return a boolean mask for a circular sector. The start/stop angles in
    `angle_range` should be given in clockwise order.
    """

    # x is a column matrix from [0,shape[0])
    # y is a row matrix from [0,shape[1])
    x, y = np.ogrid[: shape[0], : shape[1]]
    cx, cy = centre
    tmin, tmax = np.deg2rad(angle_range) if degrees == True else angle_range

    # ensure stop angle > start angle
    if tmax < tmin:
        tmax += 2 * np.pi

    # convert cartesian --> polar coordinates
    r2 = (x - cx) * (x - cx) + (y - cy) * (y - cy)
    theta = np.arctan2(x - cx, y - cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= 2 * np.pi

    # circular mask
    circmask = r2 <= radius * radius

    # angular mask
    anglemask = theta <= (tmax - tmin)

    return circmask * anglemask
