import dvpy as dv


def test_is_sorted():

    sorted_list = list(range(10))
    assert dv.is_sorted(sorted_list)

    sorted_list.reverse()
    assert not dv.is_sorted(sorted_list)
