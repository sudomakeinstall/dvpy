# System

# Third Party
import numpy as np

# Internal


def displacement_gradient_tensor(x, y):
    (dx_dx, dx_dy) = np.gradient(x)
    (dy_dx, dy_dy) = np.gradient(y)
    group = np.array([[dx_dx, dx_dy], [dy_dx, dy_dy]])
    return np.transpose(group, (2, 3, 0, 1))
