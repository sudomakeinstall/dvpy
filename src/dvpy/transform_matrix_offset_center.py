# System

# Third Party
import numpy as np

# Internal


def transform_full_matrix_offset_center(matrix, shape):
    # Check dimensions
    if matrix.ndim != 2:
        raise ValueError("The transformation matrix must have 2 dimensions.")

    if matrix.shape[0] != (len(shape) + 1):
        raise ValueError(
            "The first dimension of the transformation matrix must be equal to len(shape) + 1."
        )

    if matrix.shape[1] != (len(shape) + 1):
        raise ValueError(
            "The second dimension of the transformation matrix must be equal to len(shape) + 1."
        )

    shape = np.array([float(s) / 2.0 + 0.5 for s in shape])

    for_mat = np.eye(len(shape) + 1)
    rev_mat = np.eye(len(shape) + 1)

    for_mat[:-1, -1] = +shape
    rev_mat[:-1, -1] = -shape

    return np.dot(np.dot(for_mat, matrix), rev_mat)


def transform_partial_matrix_offset_center(matrix, shape):
    # Check dimensions
    if matrix.ndim != 2:
        raise ValueError("The transformation matrix must have 2 dimensions.")

    if matrix.shape[0] != len(shape):
        raise ValueError(
            "The first dimension of the transformation matrix must be equal to len(shape)."
        )

    if matrix.shape[1] != (len(shape) + 1):
        raise ValueError(
            "The second dimension of the transformation matrix must be equal to len(shape) + 1."
        )

    last_row = np.zeros((1, len(shape) + 1))
    last_row[0, -1] = 1
    matrix = np.concatenate([matrix, last_row], axis=0)
    matrix = transform_full_matrix_offset_center(matrix, shape)
    return matrix[:-1, :]
