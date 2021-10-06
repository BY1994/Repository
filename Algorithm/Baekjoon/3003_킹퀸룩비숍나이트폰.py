"""
3003
"""

chess = [1, 1, 2, 2, 2, 8]
his = list(map(int, input().split()))
print(*[chess[i] - his[i] for i in range(6)])
