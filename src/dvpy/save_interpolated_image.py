# System

# Third Party
import pylab as plt

# Internal


def save_interpolated_image(array, fileName, colormap="gray"):
    plt.gca().set_axis_off()
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.imshow(array, cmap=colormap)
    plt.savefig(fileName, bbox_inches="tight", pad_inches=0)
    plt.close("all")
