"""
11051 이항 계수 2
"""

pascal = [[1 for i in range(1001)] for j in range(1001)]
N, K = map(int, input().split())
for i in range(2, N+1):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        pascal[i][j] %= 10007
print(pascal[N][K])
