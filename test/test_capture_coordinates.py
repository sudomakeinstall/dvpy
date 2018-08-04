import dvpy as dv
import numpy as np
import pylab as plt
import matplotlib as mpl

# def test_capture_coordinates_from_image():
#  im = np.ones((256,256))
#  capture_object = dv.capture_coordinates_from_image(im)
#  print('\n', capture_object.x, capture_object.y)


def test_capture_coordinates():
    im = np.ones((256, 256))
    fig, ax = plt.subplots(1, 1)
    capture_object = dv.capture_coordinates(ax, im)
    cid = fig.canvas.mpl_connect("button_press_event", capture_object.onclick)

    event = mpl.backend_bases.MouseEvent("some_event", fig.canvas, 128.0, 128.0)

    capture_object.onclick(event)

    print(capture_object.x, capture_object.y)

    plt.show()
    fig.canvas.mpl_disconnect(cid)
