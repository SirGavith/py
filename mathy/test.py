import networkx as nx
import math

def isPrime(n):
    for a in range(2, math.floor(math.sqrt(n)) + 1):
        if n % a == 0: return False
    return True




for n in range(2,20):
    print('n=', n)
    prime = isPrime(n)

    for k in range(n):
        G = nx.DiGraph()

        G.add_nodes_from(range(n))

        for i in range(n):
            G.add_edge(i,i * k % n)

        weak_comopnents = len([*nx.weakly_connected_components(G)])

        if weak_comopnents == 2:
            print(n, k, 2, prime)