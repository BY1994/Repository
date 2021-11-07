"""
Atcoder B
"""

N = int(input())
ans = 0
myset = []
for _ in range(N):
    _input = tuple(input().split())
    myset.append(_input)
print(len(set(myset)))
