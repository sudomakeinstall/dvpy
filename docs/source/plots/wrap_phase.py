import pylab as plt
import dvpy as dv

d = np.arange(-10, +10, 0.1)
w = dv.wrap_phase(d)

plt.plot(d)
plt.plot(w)
plt.show()
