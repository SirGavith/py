from mathy.mathy import *
from mathy.xkmodn import *


def print_information(N: int):
    print(f'N={N}')
    print(f'Units: {units(N)}')
    print(f'Primitive roots: {primitiveRoots(N)}')
    print(f'Inverses: {inverses(N)}')
    print(f'Orders: {orders(N)}')

# N = 10

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


# Investigating n=p^t
# print(primitiveRoots(3))
# print(primitiveRoots(9))
# print(orders(27))
# print(primitiveRoots(27))
# multiPlot([1,2,3,4,5,6,7,8],[3,9,27])
# multiPlot([1,2,3,4,5,6,7,8],[3,9,27])


#Investigating k_1+k_2=n
# N = 11
# print(primitiveRoots(N))
# print(orders(N))
# print(inverses(N))
# # multiPlot([3,4,[3,4],2,5,[2,5],1,6,[1,6]],[7])
# multiPlot([3,8,[3,8],2,9,[2,9]],[11])
# multiPlot([4,7,[4,7],5,6,[5,6]],[11])

# N = 8
# multiPlot([1,7,[1,7],2,6,[2,6],3,5,[3,5]],[8])

# N = 24
# print(units(N))
# print('5,19',fixing_number(createGraph([5,19],N)))
# print('7,17',fixing_number(createGraph([7,17],N)))
# print('11,13',fixing_number(createGraph([11,13],N)))

# print(inverses(11))

# multiPlot([[3,10],[4,10]], [11])

# G1 = createGraph([3,10], 11)
# G2 = createGraph([4,10], 11)

# print(G_1_stab1)


# print(fixing_number_set(G1))
# print(fixing_number_set(G2))

# for N in [6,8,9,10,12]:
#     print_information(N)


# printFixingNumbersFor2KValuesTables()


# print(units(12))

# singlePlot(createGraph([2,6],7))

N=11
print(inverses(N))
print(orders(N))
print(primitiveRoots(N))

multiPlot([3,5,[3,5], 4,5,[4,5], 9],[N])
# multiPlot([[2,2**8], [2,2**9], [2, 1]],[N])


plt.show() 
