from dvpy import wrap_phase
import numpy as np


def test_wrap_phase():
    # Scalars
    assert np.allclose(wrap_phase(0.0), 0.0)
    assert np.allclose(wrap_phase(+1.0), +1.0)
    assert np.allclose(wrap_phase(-1.0), -1.0)
    assert np.allclose(wrap_phase(-6.0), (-6.0 + 2.0 * np.pi))
    assert np.allclose(wrap_phase(+6.0), (+6.0 - 2.0 * np.pi))

    # ndarray
    assert np.allclose(wrap_phase(np.zeros((3, 3))), np.zeros((3, 3)))
    assert np.allclose(wrap_phase(np.ones((3, 3))), np.ones((3, 3)))
    assert np.allclose(wrap_phase(np.ones((3, 3)) + 2 * np.pi), np.ones((3, 3)))

    # Matrices
    assert np.allclose(
        wrap_phase(np.matrix(np.zeros((3, 3)))), np.matrix(np.zeros((3, 3)))
    )
