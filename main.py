from math import gcd
import math
from typing import Iterable

import numpy as np

def first(iterable, condition = lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satysfing the condition is found.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    """

    return next((x for x in iterable if condition(x)), None)

def order(n, mod):
    return first(range(2, mod), lambda k : (n**k % mod == 1))

def product(iterable: Iterable[int]):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def phi(n):
    return sum(1 for i in range(1, n+1) if gcd(i,n)==1)

# print(order(8, 11))

# for n in range(1,30):
#     print(n, phi(3*n) == 3 * phi(n), n % 3)

# for x in range(0,11):
#     for y in range(0,11):
#         if (y ** 2)%11 == ((x**3) - 8*x)%11: print(x,y)

# for i in range(1, 1000000):
#     if all(i % n == 0 for n in range(2,14)):
#         print(i)
#         break

# print(product(range(2, 13)))

# print(order(24,42))

# for n in range(3,14):
#     #E k s.t. m^k == n
#     print(n, [(m,k) for m in range(1,n) if (k := first(range(1,n), lambda k : (m**k % n == 1)))])

def two_adic_valuation(n):
    if n & 1: return 0

    for i in range(1,100):
        n >>= 1
        if n & 1: return i

# def isPrime(n):
#     if type(n) is not int: raise TypeError("n must be an integer")
#     if n == 2: return True
#     if n < 1 or n % 2 == 0: return False

#     #Miller-Rabin test
#     s = two_adic_valuation(n-1)   #2-adic valuation of n-1
#     d = n // 2 ** s             #remainder of n

#     witnesses = []
#     if (n < 1373653):
#         witnesses = [2,3]
#     elif n < 25326001:
#         witnesses = [2,3,5]
#     else:
#         raise ValueError("n is too big for this prime test")

#     witnesses = [137]

#     for a in witnesses: #suffiecient witnesses up to 1.3e6
#         if (s := a**d % n) != 1 or s !=: return False
#     return True

def isPrime2(n):
    for a in range(2, math.floor(math.sqrt(n))):
        if n % a == 0: return False, a
    return True

# print(isPrime(1662803))
# print(isPrime2(1662803))
# print(isPrime(221))


# for n in range(2,10000):
#     if (n % 17 == 3) and (n % 16 == 10) and (n % 15 == 0):
#         print(n)


squares = {n**2 for n in range(1000000)}

for x in range(0,1000000):
    if (1 + 122*x*x) in squares:
        print(x, (1 + 122*x*x))