from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# TODO: FULL CODE FOUND AT https://github.com/SirGavith/py/blob/main/modernphys_ps7-2.py

#B
x,L = symbols('x L')
print('Symbolic c_n s:')
def get_c_n(n):
    psi_n = sqrt(2/L) * sin(n*pi*x/L)
    psi = sqrt(840/L**7) * x * (L - x) * (x - L/2)

    print(f'c{n} =', c_n := integrate(psi_n * psi,(x,0,L)))
    return c_n

c_ns = [get_c_n(n).evalf(subs={L: 1}) for n in range(1,5)]
print("C_n s for L=1", c_ns)

#C
def psi_n(n, x):
    return np.sqrt(2/1) * np.sin(n * np.pi * x / 1)

X = np.linspace(0,1,100)
plt.plot(X, [sum((c_ns[n - 1] * psi_n(n, x)) for n in range(1,5)) for x in X])
plt.plot(X, [sqrt(840) * x * (1 - x) * (x - 1/2) for x in X])

# The plots are pretty similar, so the contributions from n>=5 should be fairly insignificant

# D
P_ns = [c_ns[n] ** 2 for n in range(4)]
for n in range(1, 5):
    print(f"P_{n} = {P_ns[n-1]:.4f}")

# E
print(f"Sum pf P_n s = {sum(P_ns):.4f}")
print(f"Odds of energy levels >= 5: {(1 - sum(P_ns)) * 100:.2f}%")
# That number is pretty small, so it does indeed agree with my earlier prediction

# F
E_ns = [P_ns[n-1] * n**2 for n in range(1,5)]
print(f"E_ns: [{', '.join(str(round(E_n,2)) + ' * E_1' for E_n in E_ns)}]")


plt.show()