import networkx as nx
import math

def isPrime(n):
    for a in range(2, math.floor(math.sqrt(n)) + 1):
        if n % a == 0: return False
    return True

# for n in range(2,20):
#     print('n=', n)
#     prime = isPrime(n)

#     for k in range(n):
#         G = nx.DiGraph()

#         G.add_nodes_from(range(n))

#         for i in range(n):
#             G.add_edge(i,i * k % n)

#         weak_comopnents = len([*nx.weakly_connected_components(G)])

#         if weak_comopnents == 2:
#             print(n, k, 2, prime)

def cyclicSubgroup(p, k):
    H = [k]
    while H[-1] != 1:
        H.append((H[-1]*k) % p)
    return H

def order(p, k):
    return len(cyclicSubgroup(p,k))

def getCosets(p, subgroup):
    cosets = [subgroup]
    ucosets = set(subgroup)

    for k in range(1,p-1):
        if k not in ucosets:
            C = [x * k % p for x in subgroup]
            cosets.append(C)
            for x in C:
                ucosets.add(x) 

    return cosets



# H = cyclicSubgroup(7,2)
# print()

# # p=7
# # for k in range(1,p-1):
#     # print(k, cyclicSubgroup(p, k))

# print(getCosets(7,H))
