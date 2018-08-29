# System

# Third Party
import numpy as np

# Internal


def wrap_phase(x):
    """
    Wrap the input into the range (-pi, pi].
  
    :param x: Number, array, or matrix to be phase wrapped.
    :type x: array-like
  
    :returns: A structure of the same shape as the input wrapped
      into the range (-pi, pi] elementwise.
    :rtype: array-like, of same shape as the input

    .. plot::

        import pylab as plt
        import dvpy as dv

        d = np.arange(-10, +10, 0.1)
        w = dv.wrap_phase(d)

        plt.plot(d)
        plt.plot(w)
        plt.show()
    """
    return (x + np.pi) % (2.0 * np.pi) - np.pi
