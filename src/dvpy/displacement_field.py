# System

# Third Party
import numpy as np

# Internal
from .wrap_phase import wrap_phase


def displacement_field(dim, center, mag=1.0, rot=0.0):
    extent = 1.75
    (nx, ny) = dim
    (cx, cy) = center
    rdf = np.linspace(-extent, extent, nx)
    idf = np.linspace(-extent, extent, ny)
    rdf += (nx / 2.0 - cx) / (0.5 * nx)
    idf += (ny / 2.0 - cy) / (0.5 * ny)
    rdf, idf = np.meshgrid(rdf, idf)
    mag = (-np.sqrt(np.power(rdf, 2) + np.power(idf, 2)) + np.sqrt(2.0)) * mag
    arg = wrap_phase(np.angle(rdf + idf * 1.0j) + rot)
    return (mag, arg)
