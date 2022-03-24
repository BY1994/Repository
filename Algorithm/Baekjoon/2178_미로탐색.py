import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = []
visited = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    miro.append(input())

q = []
visited[0][0] = 1
qs, qe = 0, 1
q.append([0, 0, 1])

while qs < qe:
    x = q[qs][0]
    y = q[qs][1]
    dist = q[qs][2]
    qs += 1

    if x == N-1 and y == M-1:
        print(dist)
        break

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= N  or ny < 0 or ny >= M: continue
        if visited[nx][ny] == 1: continue
        if miro[nx][ny] == '0': continue
        visited[nx][ny] = 1
        q.append([nx, ny, dist+1])
        qe += 1
