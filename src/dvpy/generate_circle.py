import numpy as np


def generate_circle(cx=0.0, cy=0.0, r=1.0, N=6, counterclockwise=True, offset=0.0):
    angle = np.asarray([np.float64(i) for i in range(N)]) * 2.0 * np.pi / N
    angle += offset
    if counterclockwise:
        angle *= -1
    real = r * np.cos(angle) + cx
    imag = r * np.sin(angle) + cy
    return np.array([real, imag]).transpose()
