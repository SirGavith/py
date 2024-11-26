import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la


# A
def Vfunc(x, a, w, V0):
    if -a/2 - w/2 < x < -a/2 + w/2: return -V0
    if a/2 - w/2 < x < a/2 + w/2: return -V0
    return 0

a = 53e-12
w = 2e-12
V0 = 3.12 * 1.6e-19
N = 2000


X = np.linspace(-4*a, 4*a, N)

plt.subplot(1, 2, 1)
plt.plot(X, [Vfunc(x, a, w, V0) for x in X])

# B
m = 9.11e-31
h_bar = 1.054e-34

d = 8*a / (N-1)

H = np.zeros((N,N))
for j in range(0,N):
    if j > 0:
        H[j,j-1] = 1
    H[j,j] = -2
    if j < N-1:
        H[j,j+1] = 1
# print(H)
H *= - h_bar ** 2 / (2 * m * d ** 2)
# print(H)

for j in range(0,N):
    v = Vfunc(d*j - 4*a, a, w, V0)
    H[j,j] += v

eigenvals, eigenvecs = la.eig(H)
eigenvecs = np.transpose(eigenvecs)
eigens = list(zip(eigenvals, eigenvecs))
eigens.sort(key=lambda eigen: eigen[0])

print("smallest eigenvalues:")
print([eigen[0] for eigen in eigens[:5]])



plt.subplot(2, 2, 2)

psi_numeric = eigens[0][1]

C = np.sqrt(sum(d * psi_x**2 for psi_x in psi_numeric))

plt.plot(X, (psi_numeric / C))

plt.subplot(2, 2, 4)
plt.plot(X, (psi_numeric / C)**2)


plt.show()