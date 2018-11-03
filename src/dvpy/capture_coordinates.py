# System

# Third Party
import numpy as np

# import pylab as plt

# Internal
import dvpy as dv

# https://stackoverflow.com/questions/25521120/store-mouse-click-event-coordinates-with-matplotlib
class capture_coordinates(object):
    def __init__(self, ax, image, x=None, y=None):
        self.ax = ax
        self.shape = image.shape
        self.x = x
        self.y = y
        ax.imshow(image, cmap="gray")
        self.mask = None
        self.m = None
        self.radius = int(np.min(image.shape) / 10)
        if (x is not None) & (y is not None):
            self.update()

    def onclick(self, event):
        self.x = event.xdata
        self.y = event.ydata
        self.update()

    def update(self):
        self.m = dv.sector_mask(self.shape, (self.y, self.x), self.radius)
        if self.mask == None:
            self.mask = self.ax.imshow(self.m, alpha=0.3)
        else:
            self.mask.set_data(self.m)
        self.ax.figure.canvas.draw()


# def capture_coordinates_from_image(image, title=None, x=None, y=None):
#    fig, ax = plt.subplots(1, 1)
#    if title is not None:
#        plt.title(title)
#    capture_object = capture_coordinates(ax, image, x=x, y=y)
#    cid = fig.canvas.mpl_connect("button_press_event", capture_object.onclick)
#    plt.gca().set_axis_off()
#    plt.gca().xaxis.set_major_locator(plt.NullLocator())
#    plt.gca().yaxis.set_major_locator(plt.NullLocator())
#    plt.show()
#    fig.canvas.mpl_disconnect(cid)
#    if (capture_object.x is None) or (capture_object.y is None):
#        raise ValueError("No point was selected.")
#    return capture_object
