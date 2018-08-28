import numpy as np
import pylab as plt
import dvpy as dv

o = np.array([2.0, 2.0])
v = np.array([2.0, 1.0])
p = np.array([2.5, 3.0])

x = dv.project_point_onto_line(o, v, p)

line1 = np.array([o, o + v]).transpose()
line2 = np.array([p, x]).transpose()

size = 100

plt.plot(line1[0], line1[1], "--")
plt.plot(line2[0], line2[1], "--")

plt.scatter(*o, s=size, c="red")
plt.scatter(*(o + v), s=size, c="orange")
plt.scatter(*p, s=size, c="green")
plt.scatter(*x, s=size, c="blue")

plt.axis("equal")
plt.show()
