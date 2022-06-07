"""
17390 이건 꼭 풀어야 해!

누적합
A 범위가 1000 이라 카운트 소트 가능
"""

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + A[i-1]

for i in range(Q):
    L, R = map(int, input().split())
    print(prefix[R]-prefix[L-1])

