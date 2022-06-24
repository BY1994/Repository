"""
11441 합 구하기

구간합
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
prefix = [0]*(N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + A[i-1]
M = int(input())
for i in range(M):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])
