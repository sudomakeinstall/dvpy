import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import dvpy as dv

o = np.array([0.0, 0.0, 0.0])
n = np.array([0.0, 0.0, 2.0])
p = np.array([1.0, 1.0, 3.0])
x = dv.project_point_onto_plane(o, n, p)

n_u = dv.normalize(n)

xx, yy = np.meshgrid(
    np.arange(o[0] - 2.0, o[0] + 2.2, 1.0), np.arange(o[1] - 2.0, o[1] + 2.2, 1.0)
)

d = -np.dot(o, n_u)

zz = -(n_u[0] * xx + n_u[1] * yy + d) / n_u[2]

size = 100

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

dv.equalize_3d_axes(ax, np.array([xx, yy, zz]))
ax.plot_wireframe(xx, yy, zz)
ax.scatter(*o, c="red", s=size)
ax.scatter(*(o + n), c="orange", s=size)
ax.scatter(*p, c="green", s=size)
ax.scatter(*x, c="blue", s=size)

plt.show()
