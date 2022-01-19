"""
20155 우리 집 밑에 편의점이 있는데
"""

import sys

N, M = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
brands = [0] * (M+1)
ans = 0
for x in X:
    brands[x] += 1
    if brands[x] > ans:
        ans = brands[x]

print(ans)
