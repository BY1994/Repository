"""
4963 섬의 개수

DFS
"""

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y):
    global h, w
    for nx, ny in (x-1, y), (x, y-1), (x+1, y), (x, y+1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1):
        if nx >= h or nx < 0 or ny >= w or ny < 0:
            continue
        if mymap[nx][ny] == 0:
            continue
        mymap[nx][ny] = 0
        dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0:
        break

    mymap = []
    for i in range(h):
        mymap.append(list(map(int, input().split())))

    ans = 0
    for i in range(h):
        for j in range(w):
            if mymap[i][j] == 1:
                ans += 1
                mymap[i][j] = 0
                dfs(i, j)

    print(ans)
