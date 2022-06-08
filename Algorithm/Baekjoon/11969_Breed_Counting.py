"""
11969 Breed Counting

간단한 누적합 (prefix sum) 문제
"""

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
count  = [[0 for i in range(N)] for j in range(3)]
prefix  = [[0 for i in range(N+1)] for j in range(3)]

for i in range(N):
    count[int(input())-1][i] += 1

for i in range(3):
    for j in range(1,N+1):
        prefix[i][j] = prefix[i][j-1] + count[i][j-1]

for i in range(Q):
    a, b = map(int, input().split())
    print(prefix[0][b]-prefix[0][a-1], prefix[1][b]-prefix[1][a-1], prefix[2][b]-prefix[2][a-1])
