import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

D = 0.15 #m
m = 4/3 * np.pi * (15/2)**3 * 7.8 / 1000 #kg

lamb = 10_000 #m
gamma = 0.25 #N s^2 m^-4
g = 9.8 #m s^-2

theta = 50 * np.pi / 180
v0 = 300 #m/s
vx0 = np.cos(theta) * v0
vy0 = np.sin(theta) * v0

x0,y0 = 0,0

t = np.arange(0,48,0.1)

def c(y):
    return gamma * D * D * np.exp(-y / lamb)

def DE1(state, time):
    vx, vy, x, y = state
    v = np.sqrt(vx * vx + vy * vy)
    
    return [-c(y) * v * vx / m, -c(y) * v * vy / m - g, vx, vy]

sols = odeint(DE1, [vx0, vy0, x0, y0], t)
de1_x, de1_y = sols[:,2], sols[:,3]

for (x,y,T) in zip(de1_x,de1_y, t):
    if y < 0:
        print('de1 First y > 0 (hits the ground) at x =', x, ', t=',T)
        break

def DE2(state, time):
    vx, vy, x, y = state
    v = np.sqrt(vx * vx + vy * vy)
    
    return [-c(0) * v * vx / m, -c(0) * v * vy / m - g, vx, vy]

sols = odeint(DE2, [vx0, vy0, x0, y0], t)
de2_x, de2_y = sols[:,2], sols[:,3]

for (x,y,T) in zip(de2_x,de2_y, t):
    if y < 0:
        print('de2 First y > 0 (hits the ground) at x =', x, ', t=',T)
        break

def DE3(state, time):
    vx, vy, x, y = state    
    return [0, - g, vx, vy]

sols = odeint(DE3, [vx0, vy0, x0, y0], t)
de3_x, de3_y = sols[:,2], sols[:,3]

for (x,y,T) in zip(de3_x,de3_y, t):
    if y < 0:
        print('de3 First y > 0 (hits the ground) at x =', x, ', t=',T)
        break

plt.plot(de1_x, de1_y, color='red', label='realistic air resistance')
plt.plot(de2_x, de2_y, '--', color='blue', label='constant air resistance')
plt.plot(de3_x, de3_y, color='green', label='no air resistance')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
