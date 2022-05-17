"""
17845 수강 과목

python3 는 시간초과
pypy3 로 내서 통과
(이중 포문이 1000 * 10000 이라 1초 시간제한 안 넘어야하는데...)
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
importance = []
time = []
DP = [[0 for i in range(N+1)] for j in range(K+1)]
for i in range(K):
    I, T = map(int, input().split())
    importance.append(I)
    time.append(T)

for i in range(1, K+1):
    for j in range(N+1):
        if time[i-1] <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-time[i-1]]+importance[i-1])
        else:
            DP[i][j] = DP[i-1][j]

print(max(DP[K]))
