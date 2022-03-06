"""
RGB 거리
"""

N = int(input())
DP = [[0, 0, 0] for i in range(N)]
for i in range(N):
    R, G, B = map(int, input().split())
    DP[i][0] = R
    DP[i][1] = G
    DP[i][2] = B

    if i > 0:
        DP[i][0] += min(DP[i-1][1], DP[i-1][2])
        DP[i][1] += min(DP[i-1][0], DP[i-1][2])
        DP[i][2] += min(DP[i-1][0], DP[i-1][1])

print(min(DP[N-1]))    
