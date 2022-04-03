"""
11659 구간 합 구하기 4

누적 합
"""

import sys
input = sys.stdin.readline

prefix = [0]*100010
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(N):
    prefix[i+1] = prefix[i] + numbers[i]
for i in range(M):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])
