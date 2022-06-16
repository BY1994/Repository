"""
2740 행렬 곱셈
"""

A = []
B = []
N, M = map(int, input().split())
for _ in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))
ans = [[0 for i in range(K)] for j in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]

for i in range(N):
    print(*ans[i])
