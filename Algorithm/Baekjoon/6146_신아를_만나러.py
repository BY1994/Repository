"""
6146 신아를 만나러

BFS
"""

import sys
input = sys.stdin.readline

X, Y, N = map(int, input().split())
X, Y = X+500, Y+500
street = [[0 for i in range(1001)] for j in range(1001)]
for _ in range(N):
    A, B = map(int, input().split())
    street[A+500][B+500] = -1

q = []
qs = 0
qe = 0

street[0][0] = 1 # visited
q.append([500, 500, 0])
qe += 1

while qs < qe:
    x, y, dist = q[qs][0], q[qs][1], q[qs][2]
    qs += 1

    if x == X and y == Y:
        print(dist)
        break
    
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx > 1000 or ny < 0 or ny > 1000: continue
        if street[nx][ny] == -1: continue
        if street[nx][ny] == 1: continue
        street[nx][ny] = 1
        q.append([nx, ny, dist+1])
        qe += 1
else:
    print(0)
