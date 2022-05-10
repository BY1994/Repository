"""
2293 동전 1

대표적인 냅색 문제

동전을 바깥쪽 for 문으로 돌지 않으면
= k 를 바깥으로 돌고, 안쪽으로 n 을 돌면
순서가 다른 같은 종류 동전 사용한 경우가 계속 더해짐
1 2 나 2 1 가 모두 더해짐
하지만 for 문을 이렇게 하면 1 2 이 순서만 더해짐

j - coins[i] 이렇게 빼는 거는 if 문이 필요 없음
+ 는 방식으로 가려면 if 문을 추가해서 k 에서 멈추게 해야할 듯
"""

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    for j in range(coins[i], k+1):
        dp[j] += dp[j - coins[i]]

print(dp[k])
