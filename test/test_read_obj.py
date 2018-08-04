
import dvpy as dv


def test_read_obj():
    mesh = dv.read_obj("./test/testdata/suzanne-fixed.obj")
