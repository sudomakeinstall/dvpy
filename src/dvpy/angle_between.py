import numpy as np
import dvpy as dv

def angle_between(v1, v2):
    """
    Returns the angle in radians between vectors 'v1' and 'v2'.
    """
    v1_u = dv.normalize(v1)
    v2_u = dv.normalize(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

