
import dvpy as dv
import numpy as np
import pylab as plt


def test_wrapped_phase_difference():
    A = dv.wrap_phase(np.reshape([x for x in range(128)] * 128, (128, 128)))

    pos_phase_grad = dv.wrapped_phase_difference(A, 1)
    neg_phase_grad = dv.wrapped_phase_difference(-1 * A, 1)

    assert np.allclose(pos_phase_grad, np.ones_like(pos_phase_grad))
    assert np.allclose(neg_phase_grad, -1 * np.ones_like(neg_phase_grad))

    plt.imshow(A, "gray")
    plt.show()

    plt.imshow(dv.wrapped_phase_difference(A, 1))
    plt.show()

    plt.imshow(dv.wrapped_phase_difference(-1 * A, 1))
    plt.show()
