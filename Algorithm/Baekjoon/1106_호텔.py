"""
1106 호텔

냅색 문제

틀렸습니다를 아래 게시글 보고 해결
https://www.acmicpc.net/board/view/62732
1000 이 아니고 1100 까지 해야 
"""

import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cost = []
customer = []
DP = [100000000] * (1101)
DP[0] = 0

for i in range(N):
    a, b = map(int, input().split())
    cost.append(a)
    customer.append(b)

for i in range(1101):
    for j in range(N):
        if i >= customer[j]:
            DP[i] = min(DP[i], DP[i-customer[j]]+cost[j])

print(min(DP[C:]))
