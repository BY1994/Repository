"""
11660 구간합 구하기 5

다이나믹 프로그래밍
누적합

2차원 배열의 누적합을 왼쪽 위쪽, 왼쪽&위쪽 동시 방향 이용해서 DP 형태로 구함
a b
c d
d의 누적합을 구하려면 (0,0) 에서 b 점까지의 합과 (0,0) 부터 c 점까지의 합을 더해주고,
거기서 두번 더해진 a를 빼주면 됨

query문제라서 import sys 이거 안 해주면 input 느려서 시간초과 남
"""

import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
arr = [] # 1024 1024
prefix = [[0 for i in range(N+2)] for j in range(N+2)] # padding

for i in range(N):
    arr.append(list(map(int, input().split())))

# prefix
for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i-1][j-1]

# query
for j in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])

