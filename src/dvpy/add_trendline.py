# System

# Third Party
from scipy.stats import linregress

# Internal


def add_trendline(ax, x, y, linestyle="-", color="black"):

    reg = linregress(x, y)
    m = reg[0]
    b = reg[1]
    (x_min, x_max) = ax.get_xlim()
    ax.plot([x_min, x_max], [x_min * m + b, x_max * m + b], linestyle, color=color)
