"""
9184 DP (not submitted)
"""

DP = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                DP[i][j][k] = 1
            elif i < j and j < k:
                DP[i][j][k] += DP[i][j][k-1] + DP[i][j-1][k-1] - DP[i][j-1][k]
            else:
                DP[i][j][k] += DP[i-1][j][k] + DP[i-1][j-1][k] + DP[i-1][j][k-1] - DP[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a > 20 or b > 20 or c > 20:
        a2, b2, c2 = 20, 20, 20
    elif a <= 0 or b <= 0 or c <= 0:
        a2, b2, c2 = 0, 0, 0
    else:
        a2, b2, c2 = a, b, c
    print(f"w({a}, {b}, {c}) = {DP[a2][b2][c2]}")
