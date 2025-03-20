import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt


def calc_an(n, omega, deltatau):
    omega = 2 * np.pi / tau
    def cosn(t):
        return np.cos(n*omega*t)
    
    I =  (omega/(2 * np.pi)) * scipy.integrate.quad(cosn, -deltatau/2, deltatau/2)[0]
    return I if n == 0 else 2*I

def calc_bn(n, tau, deltatau):
    return 0

tau = 1
deltatau = 0.25

# omega = 2 * np.pi / tau

# ans = [calc_an(n, omega, deltatau) for n in range(20)]
# T = np.arange(-tau/2, tau/2, 0.01)

# plt.subplot(2,2,1)
# plt.plot(T, [1 if -deltatau/2 < t < deltatau/2 else 0 for t in T])

# plt.subplot(2,2,2)
# plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(3)) for t in T])

# plt.subplot(2,2,3)
# plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(6)) for t in T])

# plt.subplot(2,2,4)
# plt.plot(T, [sum(ans[n] * np.cos(n * omega * t) for n in range(20)) for t in T])

omega0 = 2*np.pi
tau0 = 1
beta = 0.2

def calc_An(n, omega):
    return calc_an(n, omega, deltatau)/np.sqrt((omega0**2 - n*n*omega*omega)**2+4*beta**2*n*n*omega**2)
    
def calc_deltan(n, omega):
    return np.arctan2(2*beta*n*omega, (omega0**2 - n*n*omega*omega))

T = np.arange(0, 6, 0.01)

for i,tau in zip(range(1,5), [tau0, 1.5 * tau0, 2.0 * tau0, 2.5 * tau0]):
    omega = 2 * np.pi / tau
    plt.subplot(2,2,i)
    plt.plot(T, [sum(calc_An(n, omega) * np.cos(n * omega * t - calc_deltan(n, omega)) for n in range(6)) for t in T])
    plt.ylim(-0.2,0.2)

plt.show()