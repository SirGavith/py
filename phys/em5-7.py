import numpy as np

L = 0.2
Q = 0.1e-6
e_0 = 8.854e-12

def V(y, N = 50):
    points = np.linspace(-L/2, L/2, N)
    dq = Q/N
    return (1/(4*np.pi*e_0)) * sum(dq/np.sqrt(x*x+y*y) for x in points)

V_0_01_analytic = 26947.2556489
print([V(0.01, N) / V_0_01_analytic for N in [50,500,1000,5000]])
# seems to converge to +-0.1% my analytic value around N = 1000.

V_0_1_analytic = 7921.55879178
print([V(0.1, N) / V_0_1_analytic for N in [50,400,500,1000]])
# seems to converge to +-0.1% my analytic value around N = 400.
# At N=1000, it is only off by 0.02%, so the agreement is better.
# This makes sense, becuase the further you get away, 
# the more it looks like a point charge, where N=1.
