

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

x, y, _ = EEA(101, -103)
x *= -1
y *= -1

print(x, y)

assert 101 * x - 103 * y == 1


print(x * 74, y * 74)