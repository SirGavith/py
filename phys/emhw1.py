import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

X, Y = np.meshgrid(np.arange(-5, 5, .2), np.arange(-5, 5, .2))

r = np.sqrt(X**2 + Y**2)
mask = r < 1e-10
r = np.ma.masked_where(mask, r)


plt.figure()
plt.title('a')
a = [X, Y]
Q = plt.quiver(X, Y, a[0], a[1], units='width')

plt.figure()
plt.title('b')
b = [X / r**2, Y / r**2]
Q = plt.quiver(X, Y, b[0], b[1], units='width')

plt.figure()
plt.title('c')
c = [X / r**3, Y / r**3]
Q = plt.quiver(X, Y, c[0], c[1], units='width')

plt.figure()
plt.title('d')
d = [- Y / r, X / r]
Q = plt.quiver(X, Y, d[0], d[1], units='width')

plt.show()