import dvpy as dv
import pytest as pt
import numpy as np


def test_pop_and_return():

    # An empty list is invalid.
    with pt.raises(ValueError) as err:
        dv.pop_and_return([], 0)

    # Invalid index.
    with pt.raises(ValueError) as err:
        dv.pop_and_return([1, 2, 3], -1)

    # Invalid index.
    with pt.raises(ValueError) as err:
        dv.pop_and_return([1, 2, 3], 3)

    # Normal behavior
    l = [0, 1, 2, 3]
    o = dv.pop_and_return(l, 0)
    assert np.allclose(o, [1, 2, 3])
