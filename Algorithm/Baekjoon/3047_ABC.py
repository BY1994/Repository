"""
3047 ABC

2019.04.09
"""

numbers = list(map(int, input().split()))
orders = input()

numbers.sort()

numdict = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
print(numdict[orders[0]], numdict[orders[1]], numdict[orders[2]])


"""
numbers = list(map(int, input().split()))
orders = input()

numbers.sort()

numdict = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
for o in orders:
    print(numdict[o], end=' ')

"""
