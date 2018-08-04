# System

# Third Party

# Internal


def add_horizontal_limits(ax, mu, sd):
    ax.axhline(y=mu + 1.96 * sd, color="gray", linestyle="--")
    ax.axhline(y=mu, color="black")
    ax.axhline(y=mu - 1.96 * sd, color="gray", linestyle="--")
