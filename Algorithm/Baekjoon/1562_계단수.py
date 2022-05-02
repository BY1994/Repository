"""
1562 계단 수

DP
"""

# 성공
N = int(input())

DP = [[[0 for i in range(2**10)] for j in range(10)] for k in range(N+1)]

for i in range(1,10):
    DP[1][i][1<<i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(2**10):
            # 이전 k 에 내 k 추가
            if j > 0:
                DP[i][j][k|(1<<j)] += DP[i-1][j-1][k]
                DP[i][j][k|(1<<j)] %= 1000000000

            if j < 9:
                DP[i][j][k|(1<<j)] += DP[i-1][j+1][k]
                DP[i][j][k|(1<<j)] %= 1000000000

ans = 0
for i in range(10):
    ans += DP[N][i][2**10-1]
    ans %= 1000000000

print(ans)

# 틀림
# 0~9 까지 다 포함해야함...
"""
N = int(input())
DP = [[0 for i in range(10)] for j in range(N+1)]

for i in range(1, N):
    DP[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j - 1 >= 0:
            DP[i][j] += DP[i-1][j-1]
            DP[i][j] %= 1000000000
        if j + 1 <= 9:
            DP[i][j] += DP[i-1][j+1]
            DP[i][j] %= 1000000000

print(sum(DP[N-1]))
"""
