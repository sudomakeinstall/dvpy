# System

# Third Party

# Internal


def lagrangian_strain_tensor(x):
    return 0.5 * (x.transpose() + x + x.transpose() * x)
