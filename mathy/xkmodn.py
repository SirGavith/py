# x k mod n ; k is the multiplier
import networkx as nx
import matplotlib.pyplot as plt
import math

Ks = [1,2,3,4,5,6,7,8,9,10,11]
# Ns = [1,4,8,9,10,12,16,18,20] #nonsquarefree nums
Ns = [1,2,3,5,7,11,13,17] #primes
# Ns = [4,5,6,7,8,9,10,11,12] #n

rows = len(Ns)
cols = len(Ks)

fig, axs = plt.subplots(rows, cols, constrained_layout=True)

for row, n in enumerate(Ns):
    for col, k in enumerate(Ks):
        axs[row,col].set_xticklabels([])
        axs[row,col].set_yticklabels([])
        if k > n: continue

        G = nx.DiGraph()

        G.add_nodes_from(range(1,n))

        for i in range(1,n):
            G.add_edge(i,i * k % n)

        plt.subplot2grid((rows, cols), (row, col))
        color = ['green','blue','orange','purple', 'red'][(n+k)%5]
        nx.draw(G, with_labels=True, font_color='white', node_color=color)
        # axs[row,col].set_axis_off()
        iscoprime = math.gcd(n,k) == 1
        numComponents = len([*nx.weakly_connected_components(G)])
        dividesn1 = (n-1) % (numComponents-1) if numComponents != 1 else '-'
        axs[row,col].set_title(f'{iscoprime} {numComponents} {dividesn1}')

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

# # 
# for (a,b) in ts:
#     d[a] = b
#     if a == b:
#         print('node at', a)

# print('-')
# for (a,b) in ts:
#     if a != b:
#         print(a, '->', b)

# print(d)


    

    
