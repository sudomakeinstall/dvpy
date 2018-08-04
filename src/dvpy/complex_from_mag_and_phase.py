# System

# Third Party
import numpy as np

# Internal


def complex_from_mag_and_phase(m, p):
    """
  Given magnitude and phase, create a complex number.

  :param m: magnitude
  :type m: real-valued array-like

  :param p: phase
  :type p: real-valued array-like (of same shape as m)

  :returns: Elementwise complexified array
  :rtype: complex-valued array-like (of same shape as m and p)

  """
    r = np.multiply(m, np.cos(p))
    i = np.multiply(m, np.sin(p))
    return r + i * 1.0j
