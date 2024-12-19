import numpy as np
from matplotlib import pyplot as plt

#Part a
a = 0.3

#N is the truncation, l is lambda
def FourierSum(N: int, x: int, l: int):
    def nthTerm(n: int):
        A = a / l if n == 0 else (2/(np.pi * n) * np.sin(np.pi * a * n / l))
        return A * np.cos(2 * np.pi * n * x / l)
    return sum(nthTerm(n) for n in range(N))

X = np.linspace(0, 10, 1000)

for N, col in [(1, "red"),(3, "green"),(8, "blue"),(30, "purple")]:
    plt.plot(X,[FourierSum(N, x, 1) for x in X], color=col)

#Part b
#Using truncation after 100 terms
plt.figure(2)
plt.plot(X,[FourierSum(100, x, 5) for x in X], color="red")
plt.show()