# x k mod n ; k is the multiplier
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import math

from mathy import order

Ks = [2,3,4,5,6,7,8,9]
# Ns = [1,4,8,9,10,12,16,18,20] #nonsquarefree nums
# Ns = [1,2,3,5,7,11,13,17] #primes
Ns = [3,5,15] #n

Ks = [1,2,3,4,5]
Ns = [3,5,6,15] #n

def createGraph(k: int | list[int],n) -> nx.DiGraph:
    G = nx.MultiDiGraph()
    G.add_nodes_from(range(0,n))

    if isinstance(k, int): k = [k]

    for k_i in k:
        def alpha_k_i(x):
            return x * k_i % n
        for x in range(0,n):
            G.add_edge(x, alpha_k_i(x))

    return G


def multiPlot(Ks: list[int], Ns: list[int]):
    rows = len(Ns)
    cols = len(Ks)

    fig, axs = plt.subplots(rows, cols, constrained_layout=True)
    for row, n in enumerate(Ns):
        for col, k in enumerate(Ks):
            axs[row,col].set_xticklabels([])
            axs[row,col].set_yticklabels([])

            G = createGraph(k, n)

            plt.subplot2grid((rows, cols), (row, col))
            color = ['green','blue','orange','purple', 'red'][(n+k)%5]
            nx.draw(G, with_labels=True, font_color='white', node_color=color)
            # axs[row,col].set_axis_off()

            # iscoprime = math.gcd(n,k) == 1
            # numComponents = len([*nx.weakly_connected_components(G)])
            # dividesn1 = (n-1) % (numComponents-1) if numComponents != 1 else '-'
            # axs[row,col].set_title(f'{math.gcd(n,k)} {numComponents} {dividesn1}')

    fig.canvas.draw()
    # Row labels
    for row in range(rows):
        ax = axs[row, 0]  # leftmost column
        pos = ax.get_position()
        fig.text(
            x=pos.x0 + 0.01,
            y=(pos.y0+pos.y1)/2,
            s=f'n= {Ns[row]}',
            ha='right',
            va='center',
            fontsize=12,
        )
    # Column labels
    for col in range(cols):
        ax = axs[0, col]  # top row
        pos = ax.get_position()
        fig.text(
            x=(pos.x0+pos.x1)/2,
            y=pos.y1-0.01,
            s=f'k = {Ks[col]}',
            fontsize=12
        )
    plt.show()

def singlePlot(G: nx.MultiDiGraph):
    plt.plot()
    nx.draw(G, with_labels=True, font_color='white')
    plt.show()

def automorphisms(graph: nx.MultiDiGraph) -> list[dict[int,int]]:
    return list(nx.algorithms.isomorphism.GraphMatcher(graph, graph).isomorphisms_iter())

def fixing_number_set(graph: nx.MultiDiGraph, max_fix_number = 15):
    N = graph.number_of_nodes()
    all_auts = automorphisms(graph)
    if len(all_auts) == 1:
        return 0

    # Starting at 1 and up to max_fix_number, 
    # recursively attempts to fix that many nodes.
    # Could probably be optimized to prioritize nodes that
    # make the automorphism number go down more in later steps.

    for trial_fix_num in range(1, max_fix_number):

        def recurse(auts: list[dict[int,int]], trial_fix_num_remaining: int, fixed: set[int]):
            for x in range(N):
                if x in fixed: continue
                newfixed = fixed.union(set([x]))
                # find automorphisms that fix x
                fixX = [a for a in auts if a[x] == x]

                if len(fixX) == 1: return trial_fix_num, newfixed
                elif trial_fix_num_remaining > 1:
                    fixing_n, fixing_s = recurse(fixX, trial_fix_num_remaining - 1, newfixed)
                    if fixing_n is not None:
                                return fixing_n, fixing_s
            # Failed to find fixing set of size trial_fix_num
            return None, None
        fixing_n, fixing_s = recurse(all_auts, trial_fix_num, set())
        if fixing_n is not None:
            return fixing_n, fixing_s
        
    #Fixing number greater than max_fix_number
    return None, None

def fixing_number(graph: nx.MultiDiGraph, max_fix_number = 15):
    return fixing_number_set(graph, max_fix_number)[0]


def printFixingNumbersFor2KValuesTable(N):
    print(f'N={N}')
    print('   '+' '.join([str(k) for k in range(1,N)]))
    for k_1 in range(1,N):
        fix_nums = [f'{k_1}:']
        for k_2 in range(1,N):
            if k_2 <= k_1:
                fix_nums.append('-')
            else:
                G = createGraph([k_1,k_2], N)
                # singlePlot(G)
                fix_num = fixing_number_set(G)[0]
                # print(k_1, k_2)
                fix_nums.append(str(fix_num))

        print(' '.join(fix_nums))   

def printFixingNumbersFor2KValuesTables(maxN = 15):
    for N in range(2, maxN):
        printFixingNumbersFor2KValuesTable(N)
        print()



N = 7
print(f'N={N}')
# print('   '+' '.join([str(k) for k in range(1,N)]))
for k_1 in range(1,N):
    for k_2 in range(1,N):
        if k_2 <= k_1: continue
        o_1 = order(k_1, N)
        o_2 = order(k_2, N)

        G = createGraph([k_1,k_2], N)
        G_1 = createGraph(k_1, N)
        G_2 = createGraph(k_2, N)

        # singlePlot(G)
        fix_num = fixing_number(G)
        # print(k_1, k_2)
        
        print(f'{k_1}, {k_2}: {fixing_number(G_1)}, {fixing_number(G_2)}; {fix_num}')
