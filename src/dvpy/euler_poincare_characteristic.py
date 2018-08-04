# System

# Third Party

# Internal


def euler_poincare_characteristic(vertices, edges, faces):
    """
    https://en.wikipedia.org/wiki/Euler_characteristic
    """

    return vertices - edges + faces
