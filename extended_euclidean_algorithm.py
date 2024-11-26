def EEA(a,b):    # Function that performs the Extended Euclidean Algorithm to return x,y,g such that ax+by=gcd(a,b)=g
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

for a,b in [ [60,30], [45,32], [32,45], [93,44], [44,88], [44,93],  [77,-52], [23, -5], [25,10]]:
    x,y,g = EEA(a,b)
    print(a, b, g)
    assert a * x + b * y == g

print(EEA(77,-52))
print(EEA(23, -5))
