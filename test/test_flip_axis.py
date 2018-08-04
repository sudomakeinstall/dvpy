import numpy as np
import dvpy as dv


def test_flip_axis():
    # Define an array `A`, and flipped arrays `V` and `H`.
    A = np.array([[1, 2], [3, 4]])
    V = np.array([[3, 4], [1, 2]])
    H = np.array([[2, 1], [4, 3]])

    # Flipping twice should be a no-op.
    assert np.allclose(A, dv.flip_axis(dv.flip_axis(A, 0), 0))
    assert np.allclose(A, dv.flip_axis(dv.flip_axis(A, 1), 1))

    # The first axis is vertical; the second axis is horizontal.
    assert np.allclose(A, dv.flip_axis(V, 0))
    assert np.allclose(A, dv.flip_axis(H, 1))
