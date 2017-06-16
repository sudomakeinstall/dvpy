import numpy as np
from .sector_mask import sector_mask

# https://stackoverflow.com/questions/25521120/store-mouse-click-event-coordinates-with-matplotlib
class capture_coordinates(object):
    def __init__(self, ax, image):
        self.ax = ax
        self.shape = image.shape
        self.x = None
        self.y = None
        ax.imshow(image, cmap = 'gray')
        self.mask = None
        self.m = None
        self.radius = int(np.min(image.shape) / 10)

    def onclick(self, event):
        self.x = event.xdata
        self.y = event.ydata
        self.update()

    def update(self):
        self.m = sector_mask(self.shape, (self.y, self.x), self.radius)
        if self.mask == None:
          self.mask = ax.imshow(self.m, alpha = 0.3)
        else:
          self.mask.set_data(self.m)
        ax.figure.canvas.draw()
