"""
7562 나이트의 이동

2차원 BFS
"""


import sys
input = sys.stdin.readline

for tc in range(int(input())):
    l = int(input())
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())

    visited = [[0 for i in range(l)] for j in range(l)]

    q = [[startx, starty, 0]]
    qs = 0
    qe = 1
    visited[startx][starty] = 1

    while qs < qe:
        x, y, dist = q[qs]
        qs += 1

        if x == endx and y == endy:
            print(dist)
            break

        for nx, ny in (x-1, y-2), (x-2, y-1), (x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2):
            if nx >= l or nx < 0 or ny >= l or ny < 0:
                continue
            if visited[nx][ny] == 1:
                continue
            q.append([nx, ny, dist+1])
            qe += 1
            visited[nx][ny] = 1

