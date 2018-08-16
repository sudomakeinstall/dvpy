
import dvpy as dv


def test_find_duplicates():

    dups = dv.find_duplicates(["a", "a", "b", "c", "c"])
    assert (dups - {"a", "c"}) == set([])
