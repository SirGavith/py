import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt


def calc_an(n, tau, deltatau):
    omega = 2 * np.pi / tau
    def cosn(t):
        return np.cos(n*omega*t)
    
    I =  (1/tau) * scipy.integrate.quad(cosn, -deltatau/2, deltatau/2)[0]
    return I if n == 0 else 2*I

def calc_bn(n, tau, deltatau):
    return 0

tau = 1
deltatau = 0.25
omega = 2 * np.pi / tau

ans = [calc_an(n, tau, deltatau) for n in range(20)]

T = np.arange(-tau/2, tau/2, 0.01)

plt.subplot(2,2,1)
plt.plot(T, [1 if -deltatau/2 < t < deltatau/2 else 0 for t in T])

plt.subplot(2,2,2)
plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(3)) for t in T])

plt.subplot(2,2,3)
plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(6)) for t in T])

plt.subplot(2,2,4)
plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(20)) for t in T])

omega0 = 2*np.pi
beta = 0.2

def calc_An(n):
    return 1/np.sqrt((omega0**2 - n*n*omega*omega)**2+4*beta**2*n*n*omega**2)
    
def calc_deltan(n):
    np.arctan2(2*beta*n*omega, (omega0**2 - n*n*omega*omega))


for i in range(6):
    print(i, calc_An(i), calc_deltan(i))

# plt.show()