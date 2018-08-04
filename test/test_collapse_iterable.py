import dvpy as dv


def test_collapse_iterable():
    lol = [[1, [2]], (3, 4, {5, 6}, 7), 8, "9"]

    lol_flat = dv.collapse_iterable(lol)

    assert lol_flat == [1, 2, 3, 4, 5, 6, 7, 8, "9"]
