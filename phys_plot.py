from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,5000e-9, 1000)

k0 = 1.14e7
y0 = 42 * np.cos(k0*x + 1.488) 
k1 = 2 * np.pi / 423e-9
y1 = 21 * np.cos(k1*x)

plt.plot(x,y0, color="red")
plt.plot(x,y1, color="blue")
plt.plot(x,y0+y1, color="green")
plt.show()