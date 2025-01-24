import math

def isPrime(n):
    if n == 1: return False
    for a in range(2, math.floor(math.sqrt(n)) + 1):
        if n % a == 0: return False
    return True

def primeFactors(n):
    return [p for p in range(2,n+1) if n % p == 0 and isPrime(p)]

def primeFactorization(n):
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

def factorsProduct(factors):
    prod = 1
    for p, v_p in factors.items():
        prod *= p ** v_p
    return prod



factors = {}
for n in range(1,25 + 1):
    for p, v_p in primeFactorization(n).items():
        if p in factors and factors[p] < v_p or p not in factors:
            factors[p] = v_p
    print(n, factorsProduct(factors), factors)
