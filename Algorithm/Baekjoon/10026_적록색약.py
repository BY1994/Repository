"""
10026 적록색약

dfs 혹은 bfs 로 완전탐색
"""

import sys
sys.setrecursionlimit(100000)

def dfs_c(x, y):
    global N
    for nextx, nexty in (x-1, y), (x, y-1), (x+1, y), (x, y+1):
        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N:
            continue
        if visited_c[nextx][nexty] == 1:
            continue
        if picture[nextx][nexty] == 'B':
            if picture[x][y] == 'B':
                visited_c[nextx][nexty] = 1
                dfs_c(nextx, nexty)
        else:
            if picture[x][y] != 'B':
                visited_c[nextx][nexty] = 1
                dfs_c(nextx, nexty)

def dfs_nonc(x, y):
    global N
    for nextx, nexty in (x-1, y), (x, y-1), (x+1, y), (x, y+1):
        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N:
            continue
        if visited_nonc[nextx][nexty] == 1:
            continue
        if picture[nextx][nexty] == picture[x][y]:
            visited_nonc[nextx][nexty] = 1
            dfs_nonc(nextx, nexty)

N = int(input())
picture = []
for _ in range(N):
    picture.append(input())

answerc = 0
answernonc = 0

visited_c = [[0 for i in range(N)] for j in range(N)]
visited_nonc = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if visited_c[i][j] == 0:
            answerc += 1
            visited_c[i][j] = 1
            dfs_c(i, j)
        if visited_nonc[i][j] == 0:
            answernonc += 1
            visited_nonc[i][j] = 1
            dfs_nonc(i, j)

print(answernonc, answerc)
