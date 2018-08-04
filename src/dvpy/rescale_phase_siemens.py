# System

# Third Party
import numpy as np

# Internal


def rescale_phase_siemens(x):
    x = x.astype(np.float64)
    x -= 2047.0
    x *= np.pi / 2047.0
    return x
