# System

# Third Party
import numpy as np

# Internal
import dvpy as dv


def wrapped_phase_difference(x, ax):
    padding = [[0, 0] for _ in range(2)]
    padding[ax][1] = 1
    x1 = np.pad(np.diff(x, n=1, axis=ax), padding, "edge")
    x2 = np.pad(np.diff(dv.wrap_phase(x + np.pi), n=1, axis=ax), padding, "edge")
    out = x1
    out[np.absolute(x1) > np.absolute(x2)] = x2[np.absolute(x1) > np.absolute(x2)]
    return out
