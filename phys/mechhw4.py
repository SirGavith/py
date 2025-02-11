import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# simplifying by only thinking about x and z axes, since y is always 0.

v0 = np.array([11,19])
r0 = np.array([0,0])
g = np.array([0,-9.8])

def getPosition(a, v0, x0, t):
    r = 0.5 * a * t**2 + v0 * t + x0
#   if r[1] < 0: return np.array([r[0],0])
    return r

# part a
t = np.linspace(0,2,100)
# v = np.array([11-0*t,19-g*t]) + g*t
v = np.array([g * T + v0 for T in t]).transpose()
v_2 = v.transpose()[-1]
r = np.array([getPosition(g, v0, r0, T) for T in t]).transpose()
r_2 = r.transpose()[-1]

print(v_2,r_2)

#part c


dv1 = np.array([10,5])
dv2 = np.array([-15,10])
dv3 = np.array([-15,-36.67])
dv3 = (-0.6*dv1-0.25*dv2)/0.15

t = np.arange(0,12,0.001)

r_firstchunk = np.array([getPosition(g, v_2+dv1, r_2, T) for T in t]).transpose()
r_secondchunk = np.array([getPosition(g, v_2+dv2, r_2, T) for T in t]).transpose()
r_thirdchunk = np.array([getPosition(g, v_2+dv3, r_2, T) for T in t]).transpose()

com = r_firstchunk * 0.6 + r_secondchunk * 0.25 + r_thirdchunk * 0.15


plt.plot(r[0],r[1], label='Grenade')
plt.plot(r_firstchunk[0],r_firstchunk[1], label='First chunk')
plt.plot(r_secondchunk[0],r_secondchunk[1], label='Second chunk')
plt.plot(r_thirdchunk[0],r_thirdchunk[1], label='Third chunk')
plt.plot(com[0],com[1], label='Center of mass')


#d
for chunk, name in [(r_firstchunk, 'first chunk'), (r_secondchunk, 'second chunk'), (r_thirdchunk, 'third chunk')]:
    for x,z,T in zip(*chunk, t):
        if z < 0:
            print(f'{name} hit ground at ({x:.2f},{z:.2f}), at t={T:.2f}')
            break


plt.xlim(0,80)
plt.ylim(0,30)
plt.legend()
plt.show()