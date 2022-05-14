"""
9084 동전

DP
"""
# 통과
for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1

    for i in range(N):
        for j in range(coins[i], M+1):
            dp[j] += dp[j-coins[i]]
            
    print(dp[M])

# 이렇게 하면 예제도 안 나옴...
"""
T = int(input())
for tc in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    money = [0] * (M+1)
    money[0] = 1
    for cur in range(M):
        for add in coins:
            if cur + add > M:
                break
            money[cur+add] += money[cur]

    print(money[M])
"""
