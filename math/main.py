from math import gcd
import math
from typing import Iterable

import numpy as np

from math.iterable_helpers import first

# a | b iff Exists k s.t. ak = b
def divides(a, b):
    return b % a == 0

# Order of n mod m
def order(n, mod):
    return first(range(2, mod), lambda k : (n**k % mod == 1))

# Euler's phi function
def phi(n):
    return sum(1 for i in range(1, n+1) if gcd(i,n)==1)

# Function that performs the Extended Euclidean Algorithm to return x,y,g such that ax+by=gcd(a,b)=g
def EEA(a,b):    
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


def two_adic_valuation(n):
    if n & 1: return 0

    for i in range(1,100):
        n >>= 1
        if n & 1: return i


def isPrime(n):
    for a in range(2, math.floor(math.sqrt(n))):
        if n % a == 0: return False, a
    return True
