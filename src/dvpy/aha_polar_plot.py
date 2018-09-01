# System

# Third Party
import numpy as np

# Internal


def aha_polar_plot(ax, B, E, A, P, color_mapper, linewidth=0, bounding_radius=1.0):

    data = []
    if B is not None:
        assert len(B) == 6
        data = data + list(B)
    if E is not None:
        assert len(E) == 6
        data = data + list(E)
    if A is not None:
        assert len(A) == 4
        data = data + list(A)
    if P is not None:
        assert len(P) == 1
        data = data + list(P)

    assert len(data) > 0

    TWO_PI = np.pi * 2

    # 17-Segment AHA
    # Basal, equatorial, apical, apex
    thetas = (
        [(i + 1) * TWO_PI / 6 for i in range(6)] * 2
        + [(i + 0.5) * TWO_PI / 4 for i in range(4)]
        + [0]
    )
    heights = [2. / 7] * 16 + [1. / 7]
    widths = [TWO_PI / 6] * 12 + [TWO_PI / 4] * 4 + [TWO_PI]
    inner_radii = (
        [bounding_radius * 5. / 7] * 6
        + [bounding_radius * 3. / 7] * 6
        + [bounding_radius * 1. / 7] * 4
        + [0]
    )

    ax.axis("off")
    ax.set_aspect("equal")

    bbox_props = dict(boxstyle="round,pad=0.2", fc="white", ec=None, lw=0, alpha=0.8)

    ########
    # Base #
    ########

    if B is not None:
        ax.bar(
            np.array(thetas[0:6]) + np.pi / 6.0,
            heights[0:6],
            width=widths[0:6],
            bottom=inner_radii[0:6],
            fill=True,
            linewidth=linewidth,
            color=color_mapper.to_rgba(B),
        )

        for i in range(0, 6):
            ax.text(
                thetas[i] + widths[i] / 2,
                inner_radii[i] + heights[i] / 2,
                str(i + 1),
                ha="center",
                va="center",
                bbox=bbox_props,
            )

    ################
    ## Equatorial ##
    ################

    if E is not None:
        ax.bar(
            np.array(thetas[6:12]) + np.pi / 6.0,
            heights[6:12],
            width=widths[6:12],
            bottom=inner_radii[6:12],
            fill=True,
            linewidth=linewidth,
            color=color_mapper.to_rgba(E),
        )

        for i in range(6, 12):
            ax.text(
                thetas[i] + widths[i] / 2,
                inner_radii[i] + heights[i] / 2,
                str(i + 1),
                ha="center",
                va="center",
                bbox=bbox_props,
            )

    ############
    ## Apical ##
    ############

    if A is not None:
        ax.bar(
            np.array(thetas[12:16]) + np.pi / 4.0,
            heights[12:16],
            width=widths[12:16],
            bottom=inner_radii[12:16],
            fill=True,
            linewidth=linewidth,
            color=color_mapper.to_rgba(A),
        )

        for i in range(12, 16):
            ax.text(
                thetas[i] + widths[i] / 2,
                inner_radii[i] + heights[i] / 2,
                str(i + 1),
                ha="center",
                va="center",
                bbox=bbox_props,
            )

    ##########
    ## Peak ##
    ##########

    if P is not None:
        ax.bar(
            thetas[16],
            heights[16],
            width=widths[16],
            bottom=inner_radii[16],
            fill=True,
            linewidth=0,
            color=color_mapper.to_rgba(P),
        )

        ax.text(0, 0, str(16 + 1), ha="center", va="center", bbox=bbox_props)

    ############
    ## Labels ##
    ############

    ost = 1.1
    ax.text(0, ost, "Lat", ha="center", va="center", bbox=bbox_props)
    ax.text(np.pi / 2, ost, "Ant", bbox=bbox_props, ha="center", va="center")
    ax.text(np.pi, ost, "Sep", bbox=bbox_props, ha="center", va="center")
    ax.text(3 * np.pi / 2, ost, "Inf", bbox=bbox_props, ha="center", va="center")


#  return fig
