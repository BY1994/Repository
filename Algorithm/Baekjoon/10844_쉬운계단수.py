"""
10844 쉬운 계단수

DP
"""

n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]
for i in range(1,10):# 0 으로 시작하는 수는 계단수가 아니다
    dp[0][i] = 1

for i in range(n):
    for j in range(10):
        if j > 0:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] %= 1000000000
        if j < 9:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= 1000000000

print(sum(dp[n-1])%1000000000)
