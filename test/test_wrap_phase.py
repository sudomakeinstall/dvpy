from dvpy import wrap_phase
import numpy as np

def test_wrap_phase():
  assert(np.allclose(wrap_phase( 0.0),   0.0               ))
  assert(np.allclose(wrap_phase(+1.0),  +1.0               ))
  assert(np.allclose(wrap_phase(-1.0),  -1.0               ))
  assert(np.allclose(wrap_phase(-6.0), (-6.0 + 2.0 * np.pi)))
  assert(np.allclose(wrap_phase(+6.0), (+6.0 - 2.0 * np.pi)))
