import dvpy as dv
import pylab as plt
import matplotlib as mpl

plt.rcParams["font.family"] = "serif"

colors = [(0.0, 0.0, 1.0), (1.0, 0.0, 0.0), (1.0, 1.0, 0.0)]

cmap = mpl.colors.LinearSegmentedColormap.from_list("SQUEEZ", colors, N=256)


def test_aha_polar_plot():

    fig = plt.figure(figsize=(7, 7))

    gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[15, 1])
    ax = plt.subplot(gs[0], projection="polar")
    cb = plt.subplot(gs[1])

    LAD = 0
    RCA = 1
    LCX = 2

    coronary = [
        LAD,
        LAD,
        RCA,
        RCA,
        LCX,
        LCX,
        LAD,
        LAD,
        RCA,
        RCA,
        LCX,
        LCX,
        LAD,
        LAD,
        RCA,
        LCX,
        LAD,
    ]

    minimum = 0
    maximum = 2

    norm = mpl.colors.Normalize(vmin=minimum, vmax=maximum, clip=True)
    mapper = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

    mpl.colorbar.ColorbarBase(cb, cmap=cmap, norm=norm, orientation="horizontal")

    dv.aha_polar_plot(
        ax,
        coronary[0:6],  # Base
        coronary[6:12],  # Mid
        coronary[12:16],  # Apex
        [coronary[16]],  # Peak
        mapper,
    )

    plt.show()
