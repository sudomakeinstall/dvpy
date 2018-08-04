# System

# Third Party
from scipy.stats import linregress

# Internal
import dvpy as dv


def annotate_linear_regression(x, y, x_label="x", y_label="y"):
    reg = linregress(x, y)
    m = reg[0]
    b = reg[1]
    r = reg[2]
    p = reg[3]
    p = dv.format_p_value(p)

    return "$%s = %.2f %s + %.2f$\n$R = %.2f$ ($%s$)" % (y_label, m, x_label, b, r, p)
