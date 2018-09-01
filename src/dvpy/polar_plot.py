# System

# Third Party
import numpy as np

# Internal


def polar_plot(ax, data, offsets=None, color_mapper=None, bounding_radius=7.0):

    if offsets == None:
        offsets = [0.0] * len(data)
    height = bounding_radius / (len(data) * 2)

    for i, d in enumerate(data):
        inner_radius = i * height
        width = np.pi * 2.0 / len(d)
        thetas = [(x + 0.5) * width + offsets[i] for x in range(len(d))]

        ax.bar(
            thetas,
            [height] * len(d),
            [width] * len(d),
            bottom=[inner_radius] * len(d),
            fill=True,
            color=color_mapper.to_rgba(d) if color_mapper is not None else None,
        )

    ax.axis("off")
    ax.set_aspect("equal")
