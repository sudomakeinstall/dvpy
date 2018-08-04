import dvpy as dv
import pylab as plt
import matplotlib as mpl
import numpy as np

plt.rcParams["font.family"] = "serif"

colors = [(0.0, 0.0, 1.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0)]

cmap = mpl.colors.LinearSegmentedColormap.from_list("SQUEEZ", colors, N=256)


def test_polar_plot():

    # The data is a list of lists of numbers.
    # Each sublist represents one ring of the polar plot (from outermost to innermost).
    data = np.random.randint(0, 5, (9, 30))

    fig = plt.figure(figsize=(7, 7))

    ax = fig.add_subplot(1, 1, 1, projection="polar")

    minimum = 0
    maximum = 4

    norm = mpl.colors.Normalize(vmin=minimum, vmax=maximum, clip=True)
    mapper = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

    dv.polar_plot(ax, data, color_mapper=mapper)

    plt.show()
