"""
7576 토마토

BFS
"""
box = []
N, M = map(int, input().split())
for _ in range(M):
    box.append(input().split())

tomatos = 0
for i in range(M):
    for j in range(N):
        if box[i][j] == '0':
            tomatos += 1

q = []
qs = 0
qe = 0

visited = [[0 for i in range(N)] for j in range(M)]
for i in range(M):
    for j in range(N):
        if box[i][j] == '1':
            visited[i][j] = 1
            q.append((i, j, 0))
            qe += 1

while qs < qe:
    x, y, day = q[qs]
    qs += 1

    for nextx, nexty in (x-1, y), (x, y-1), (x+1, y), (x, y+1):
        if nextx < 0 or nextx >= M or nexty < 0 or nexty >= N:
            continue
        if visited[nextx][nexty] == 1:
            continue

        if box[nextx][nexty] == '0':
            q.append((nextx, nexty, day+1))
            box[nextx][nexty] = '1'
            visited[nextx][nexty] = 1
            qe += 1
            tomatos -= 1

if tomatos > 0:
    print(-1)
else:
    print(day)

