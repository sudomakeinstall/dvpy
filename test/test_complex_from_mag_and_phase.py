from dvpy import complex_from_mag_and_phase
import numpy as np

def test_complex_from_mag_and_phase():
  assert(np.allclose(complex_from_mag_and_phase(1.0,     0.0      ),  1.0 ))
  assert(np.allclose(complex_from_mag_and_phase(1.0,     np.pi / 2),  1.0j))
  assert(np.allclose(complex_from_mag_and_phase(1.0,     np.pi    ), -1.0 ))
  assert(np.allclose(complex_from_mag_and_phase(1.0, 3 * np.pi / 2), -1.0j))
