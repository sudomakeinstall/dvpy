import dvpy as dv
import numpy as np


def test_segmentation_metrics():

    t = np.ones((2, 2)) * 5
    p = np.ones((2, 2)) * 5

    j_1 = dv.jaccard_index(t, p, 5)
    d_1 = dv.dice_coefficient(t, p, 5)

    assert np.allclose(j_1, 1.00)
    assert np.allclose(d_1, 1.00)
    assert np.allclose(j_1, dv.dice_to_jaccard(d_1))
    assert np.allclose(d_1, dv.jaccard_to_dice(j_1))

    p[0, 0] = 1

    j_2 = dv.jaccard_index(t, p, 5)
    d_2 = dv.dice_coefficient(t, p, 5)

    assert np.allclose(j_2, 0.75)
    assert np.allclose(d_2, 2 * 0.75 / 1.75)
    assert np.allclose(j_2, dv.dice_to_jaccard(d_2))
    assert np.allclose(d_2, dv.jaccard_to_dice(j_2))

    p[0, 1] = 2

    j_3 = dv.jaccard_index(t, p, 5)
    d_3 = dv.dice_coefficient(t, p, 5)

    assert np.allclose(j_3, 0.50)
    assert np.allclose(d_3, 2 * 0.50 / 1.50)
    assert np.allclose(j_3, dv.dice_to_jaccard(d_3))
    assert np.allclose(d_3, dv.jaccard_to_dice(j_3))

    p[1, 0] = 3

    j_4 = dv.jaccard_index(t, p, 5)
    d_4 = dv.dice_coefficient(t, p, 5)

    assert np.allclose(j_4, 0.25)
    assert np.allclose(d_4, 2 * 0.25 / 1.25)
    assert np.allclose(j_4, dv.dice_to_jaccard(d_4))
    assert np.allclose(d_4, dv.jaccard_to_dice(j_4))

    p[1, 1] = 4

    j_5 = dv.jaccard_index(t, p, 5)
    d_5 = dv.dice_coefficient(t, p, 5)

    assert np.allclose(j_5, 0.00)
    assert np.allclose(d_5, 0.00)
    assert np.allclose(j_5, dv.dice_to_jaccard(d_5))
    assert np.allclose(d_5, dv.jaccard_to_dice(j_5))
