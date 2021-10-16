"""
1463 1로 만들기
DP

RecursionError 발생
https://help.acmicpc.net/judge/rte/RecursionError

답 안 나오는 반례
https://www.acmicpc.net/board/view/74954
* 3 , *2, +1 순으로 하면 무조건 최소일 거라고 생각해서
0 이면 d 값으로 대체하게만 했는데,
그게 무조건 최소는 아니다.
그래서 반례 케이스는 통과 못했고, memo를 max 값,
memo[x] > d 조건 넣으니까 반례 통과했다.

1000000 넣으면 시간 초과 나는 것 같은데...
memo 크기를 +1을 빼먹었더니 런타임 에러가 났다...
"""
N = int(input())
memo = [10**6+1] * (10**6+1)

memo[1] = 0
memo[2] = 1
memo[3] = 1

for i in range(4, N+1):
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3])
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2])
    memo[i] = min(memo[i], memo[i-1])
    memo[i] += 1
print(memo[N])


# RecursionError
# => 메모리 초과
"""
import sys
sys.setrecursionlimit(10**6)

def dp(x, N, d):
    if x > N:
        return 0
    if memo[x] > d:
        #print(f"{x}:{d}\n")
        memo[x] = d
        dp(x*3, N, d+1)
        dp(x*2, N, d+1)
        dp(x+1, N, d+1)

N = int(input())
memo = [10**6+1] * (N+1)
dp(1, N, 0)
print(memo[N])
"""

# 샘플 풀이 이해 안 됨
# -1 한 거가 min 할 때 따로 하나로 고려되어야할 것 같은데 그게 없음
# https://www.acmicpc.net/source/25454228

"""
# dp
def dp(n):
    if n in memo:
        return memo[n]
    # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
    # 이 경우를 나머지로 더해주는 것으로 짐작된다.
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
    memo[n] = m
    return m


memo = {1: 0, 2: 1}
n = int(input())
print(dp(n))
"""
