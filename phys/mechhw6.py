import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt


r = np.arange(0,10,0.01)

A = 1
S = 1
R = 200

def U(r):
    return A * ((np.exp((R-r)/S)-1)**2 - 1)

plt.plot(r, [U(rr) for rr in r])

plt.show()