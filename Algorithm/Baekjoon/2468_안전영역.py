"""
2468 안전 영역

완전 탐색

k 를 1부터 했을 때 반례가 있었다.
3
1 1 1
1 1 1
1 1 1

하면 답이 1이 나와야하는데, k를 1부터 돌면 답이 0이 나와버린다.
"""

import sys
sys.setrecursionlimit(100000000)

def dfs(k, x, y):
    global N
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if region[nx][ny] <= k:
            continue
        if visited[k][nx][ny] == 1:
            continue
        visited[k][nx][ny] = 1
        dfs(k, nx, ny)

N = int(input())
region = []
for i in range(N):
    region.append(list(map(int, input().split())))
visited = [[[0 for i in range(N)] for j in range(N)] for k in range(101)]

ans = 0
for k in range(101):
    cur = 0
    for i in range(N):
        for j in range(N):
            if region[i][j] <= k:
                continue
            if visited[k][i][j] == 1:
                continue
            visited[k][i][j] = 1
            cur += 1
            dfs(k, i, j)
    ans = max(ans, cur)

print(ans)
