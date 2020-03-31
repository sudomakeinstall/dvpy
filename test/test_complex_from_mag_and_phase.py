import dvpy as dv
import numpy as np


def test_complex_from_mag_and_phase():
    # Test Scalars
    assert np.allclose(dv.complex_from_mag_and_phase(1.0, 0.0), 1.0)
    assert np.allclose(dv.complex_from_mag_and_phase(1.0, np.pi / 2), 1.0j)
    assert np.allclose(dv.complex_from_mag_and_phase(1.0, np.pi), -1.0)
    assert np.allclose(dv.complex_from_mag_and_phase(1.0, 3 * np.pi / 2), -1.0j)

    # Test NDArray
    ones = np.ones((3, 3))
    zeros = np.zeros((3, 3))
    assert np.allclose(dv.complex_from_mag_and_phase(ones, zeros), ones)

    # Test Matrices
    ones = np.array(ones)
    zeros = np.array(zeros)
    assert np.allclose(dv.complex_from_mag_and_phase(ones, zeros), ones)
