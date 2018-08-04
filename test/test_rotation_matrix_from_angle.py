import dvpy as dv
import numpy as np


def test_rotation_matrix_from_angle():

    print(dv.rotation_matrix_from_angle(np.pi / 2))
    print(dv.rotation_matrix_from_angle(np.pi / 2, matrix_type="yaw"))
    print(dv.rotation_matrix_from_angle(np.pi / 2, matrix_type="pitch"))
    print(dv.rotation_matrix_from_angle(np.pi / 2, matrix_type="roll"))
