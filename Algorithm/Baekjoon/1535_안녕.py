"""
1535 안녕

냅색 문제
DP[아이템][무게] = 최대가치

문제에서 체력이 100 이라고 주어져서, 100 까지 사용하려고 했는데,
예제 1을 보면 100 까지 사용할 수 없음
100 을 다 쓰면 죽는 상태라 가면 안 되는 것으로 보임

-1 을 인덱스로 썼는데 파이썬이라 문제가 없었음
본 문제에서 반례에 걸렸음
"""

N = int(input())
power = list(map(int, input().split()))
happy = list(map(int, input().split()))

DP = [[0 for i in range(100)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(100):
        if power[i-1] <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-power[i-1]]+happy[i-1])
        else:
            DP[i][j] = DP[i-1][j]

print(max(DP[N]))

# 틀렸습니다
"""
N = int(input())
power = list(map(int, input().split()))
happy = list(map(int, input().split()))

DP = [[0 for i in range(100)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(100):
        if power[i-1] <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-power[i-1]]+happy[i-1])
        else:
            DP[i][j] = DP[i-1][j]

print(max(DP[N]))
"""
