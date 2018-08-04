# System

# Third Party
import numpy as np

# Internal


def physical_coordinates(extent, spacing=(1, 1), origin=(0, 0)):
    (nx, ny) = extent
    (sx, sy) = spacing
    (ox, oy) = origin

    x = np.linspace(ox, ox + nx * sx, nx)
    y = np.linspace(oy, oy + ny * sy, ny)

    return np.meshgrid(x, y)
