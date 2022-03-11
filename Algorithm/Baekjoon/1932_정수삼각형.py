"""
1932 정수 삼각형
"""

n = int(input())
DP = [[0 for i in range(n+1)] for j in range(n+1)]
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1):
        DP[i][j] += triangle[i][j]
        DP[i+1][j] = max(DP[i][j], DP[i+1][j])
        DP[i+1][j+1] = max(DP[i][j], DP[i+1][j+1])

print(max(DP[n-1]))
