"""
7569 토마토

BFS
in 3-dimension
"""

M,N,H = map(int, input().split())

boxes = []
for i in range(H):
    box = []
    for j in range(N):
        box.append(input().split())
    boxes.append(box)

visited = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
q = []

qs = 0
qe = 0

tomatos = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == '0':
                tomatos += 1
            elif boxes[i][j][k] == '1':
                visited[i][j][k] = 1
                q.append((i, j, k, 0))
                qe += 1

while qs < qe:
    z,x,y,day = q[qs]
    qs += 1

    for nextx, nexty, nextz in (x, y, z-1), (x, y, z+1), (x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z):
        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= M or nextz < 0 or nextz >= H:
            continue
        if visited[nextz][nextx][nexty] == 1:
            continue
        if boxes[nextz][nextx][nexty] == '0':
            visited[nextz][nextx][nexty] = 1
            q.append((nextz, nextx, nexty, day+1))
            qe += 1
            tomatos -= 1

if tomatos > 0:
    print(-1)
else:
    print(day)
