from math import gcd
import math
from typing import Iterable

import numpy as np

from iterable_helpers import first

# Returns true iff n is prime
def isPrime(n: int) -> bool:
    if n == 1: return False
    for a in range(2, math.floor(math.sqrt(n)) + 1):
        if n % a == 0: return False
    return True

# Returns a list of the prime factors of n
def primeFactors(n: int) -> list[int]:
    return [p for p in range(2,n+1) if n % p == 0 and isPrime(p)]

# Returns a map with keys the prime factors of n and values their p-adic valuations
def primeFactorization(n: int) -> map[int,int]:
    primes = [p for p in range(2,n + 1) if isPrime(p)]
    factors = {}
    i = 0
    while n > 1:
        p = primes[i]
        if n % p == 0:
            n /= p
            if p in factors:
                factors[p] += 1
            else:
                factors[p] = 1
        else:
            i += 1
    return factors

# a | b iff Exists k s.t. ak = b
def divides(a: int, b: int) -> bool:
    return b % a == 0

# Order of k mod n
# Equivalently, the order of k in Z/(n)
def order(k: int, n: int) -> int:
    if k == 1: return 1
    return first(range(2, n), lambda k : (k**k % n == 1))

# Returns a list of the units of Z/(n)
def units(n: int) -> list[int]:
    u = []
    for x in range(n):
        for y in range(n):
            if (x * y) % n == 1:
                u.append(x)
                break
    return u

# Euler's phi function
def phi(n):
    return sum(1 for i in range(1, n+1) if gcd(i,n)==1)

# Function that performs the Extended Euclidean Algorithm to return x,y,g such that ax+by=gcd(a,b)=g
def EEA(a: int, b: int) -> tuple[int,int,int]:
    # if a == b: return 1, 0, a
    r0, r1 = a, b
    q=[]

    while r0 % r1 != 0:
        q.append(r0//r1)
        r0, r1 = r1, r0 % r1

    if len(q) == 0:
        return 0, 1, b
    x,y = 1, -q.pop()

    while len(q) >= 1:
        x,y = y, x - y * q.pop()

    return x, y, r1

# run some tests for the Extended Euclidean Algorithm
def test_EEA():
    for a,b in [ [60,30], [45,32], [32,45], [93,44], [44,88], [44,93],  [77,-52], [23, -5], [25,10]]:
        x,y,g = EEA(a,b)
        assert a * x + b * y == g

# Returns the 2-adic valuation of n; That is, the number of factors of two that divide n
def two_adic_valuation(n):
    if n & 1: return 0
    for i in range(1,100):
        n >>= 1
        if n & 1: return i