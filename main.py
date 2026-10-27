from mathy.mathy import *
from mathy.xkmodn import *


N = 7

# print(f'N={N}')
# print('   '+' '.join([str(k) for k in range(1,N)]))
# for k_1 in range(1,N):
#     for k_2 in range(1,N):
#         if k_2 <= k_1: continue
#         o_1 = order(k_1, N)
#         o_2 = order(k_2, N)

#         G = createGraph([k_1,k_2], N)
#         G_1 = createGraph(k_1, N)
#         G_2 = createGraph(k_2, N)

#         # singlePlot(G)
#         fix_num = fixing_number(G)
#         # print(k_1, k_2)
        
#         print(f'{k_1}, {k_2}: {fixing_number(G_1)}, {fixing_number(G_2)}; {fix_num}')

# print(inverses(N))
# multiPlot([[2, 3], [2, 4], [2, 5], [2, 6]], [N])
# multiPlot([[3, 4],[3, 5],[3, 6]], [N])

# G = createGraph([6,10], N)
# print(fixing_number_set(G))
# singlePlot(G)

# multiPlot([1,2,3,4,5,6,7,8],[2,4,8,16])
multiPlot([1,2,3,4,5,6,7,8],[3,9,27])

plt.show()
