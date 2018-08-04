# System

# Third Party

# Internal


def format_p_value(p):
    assert (p <= 1.0) & (p >= 0.0)

    if p < 0.0001:
        return "p < 0.0001"
    elif p < 0.001:
        return "p < 0.001"
    elif p < 0.01:
        return "p < 0.01"
    elif p <= 0.05:
        return "p = %.2f" % (p)
    else:
        return "p = NS"
