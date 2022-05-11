"""
3067 Coins

냅색 문제
"""

for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    DP = [0]*(M+1)
    DP[0] = 1

    for i in range(N):
        for j in range(coins[i], M+1):
            DP[j] += DP[j - coins[i]]

    print(DP[M])
