"""
2206 벽 부수고 이동하기

BFS
"""

N, M = map(int, input().split())
visited = [[[0 for i in range(2)] for j in range(M)] for k in range(N)]

board = []
for i in range(N):
    board.append(input())

q = [[0, 0, 0, 1]]
qs = 0
qe = 1
visited[0][0][0] = 1

while qs < qe:
    x, y, broken, dist = q[qs]
    qs += 1

    if x == N-1 and y == M-1:
        print(dist)
        break

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == '1':
            # 벽일 때
            if broken == 0:
                q.append([nx, ny, 1, dist+1])
                qe += 1
                visited[nx][ny][1] = 1
        else:
            if visited[nx][ny][broken] == 1:
                continue
            q.append([nx, ny, broken, dist+1])
            qe += 1
            visited[nx][ny][broken] = 1            
else:
    print(-1)
