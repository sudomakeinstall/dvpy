# System

# Third Party
import numpy as np

# Internal


def normalize(vector):
    "Given a vector, return a vector with the same direction and unit magnitude."
    return vector / np.linalg.norm(vector)
