# System

# Third Party
import numpy as np

# Internal
import dvpy as dv


def rotate_2d_vector(vec, ang):
    return np.dot(dv.rotation_matrix_from_angle(ang), vec)
