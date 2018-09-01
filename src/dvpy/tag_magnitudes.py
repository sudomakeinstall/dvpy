# System

# Third Party
import numpy as np

# Internal
import dvpy as dv


def tag_magnitudes(x, y, t, T1=850, flip_angle=np.pi / 4, tag_rotation=0.0):
    fade = np.exp(-t / T1)
    o = np.sin(2 * flip_angle) * fade

    points = np.transpose(np.array((x, y)), (1, 2, 0))

    ro = dv.distance_from_points_to_plane(
        points, np.array((0, 0)), np.array((np.cos(tag_rotation), np.sin(tag_rotation)))
    )
    pe = dv.distance_from_points_to_plane(
        points,
        np.array((0, 0)),
        np.array((np.cos(tag_rotation + np.pi / 2), np.sin(tag_rotation + np.pi / 2))),
    )

    ro_1 = (np.cos(ro) * o + 2.0 - o) / 2.0
    ro_2 = (np.sin(ro) * o + 2.0 - o) / 2.0
    pe_1 = (np.cos(pe) * o + 2.0 - o) / 2.0
    pe_2 = (np.sin(pe) * o + 2.0 - o) / 2.0

    return (ro_1, ro_2, pe_1, pe_2)
