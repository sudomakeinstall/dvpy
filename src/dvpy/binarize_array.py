# System

# Third Party
import numpy as np

# Internal


def binarize_array(x):
    r = x.copy()
    r[r != 0] = 1
    return r
