"""
이미 앞으로 전진한 애가 다시 뒤를 돌아보고 S 를 찾았다고 응답함

=> 시작점을 가로세로왼쪽오른쪽 가게 시키고
거기서 한번 더 진행 시킴
별도의 큐로 bfs 돌게 함
(그래야 뒤로 돌아보고 S 로 오지 않을 테니까)
"""
H, W = map(int, input().split())
grid = []
for i in range(H):
    grid.append(input())
    for j in range(W):
        if grid[i][j] == 'S':
            start = [i, j]

visited = [[0 for i in range(W)] for j in range(H)]
ans = 0
q = []
qs, qe = 0, 0
visited[start[0]][start[1]] = 1
# 상하좌우를 넣기
# 위로
if start[0]-1 >= 0 and grid[start[0]-1][start[1]] != '#':
    visited[start[0]-1][start[1]] = 1
    q.append([start[0]-1, start[1]])
    qe += 1

nextq = []
nextqs, nextqe = 0, 0
while qs < qe:
    curx, cury = q[qs]    
    qs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

while nextqs < nextqe:
    curx, cury = nextq[nextqs]
    nextqs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif grid[nx][ny] == 'S':
            ans = 1
            nextqs = nextqe
            break
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1
# 아래
if start[0]+1 < H and grid[start[0]+1][start[1]] != '#':
    visited[start[0]+1][start[1]] = 1
    q.append([start[0]+1, start[1]])
    qe += 1


nextq = []
nextqs, nextqe = 0, 0
while qs < qe:
    curx, cury = q[qs]    
    qs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

while nextqs < nextqe:
    curx, cury = nextq[nextqs]
    nextqs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif grid[nx][ny] == 'S':
            ans = 1
            nextqs = nextqe
            break
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

# 오른쪽
if start[1]+1 < W and grid[start[0]][start[1]+1] != '#':
    visited[start[0]][start[1]+1] = 1
    q.append([start[0], start[1]+1])
    qe += 1

nextq = []
nextqs, nextqe = 0, 0
while qs < qe:
    curx, cury = q[qs]    
    qs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

while nextqs < nextqe:
    curx, cury = nextq[nextqs]
    nextqs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif grid[nx][ny] == 'S':
            ans = 1
            nextqs = nextqe
            break
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

# 왼쪽
if start[1]-1 >= 0 and grid[start[0]][start[1]-1] != '#':
    visited[start[0]][start[1]-1] = 1
    q.append([start[0], start[1]-1])
    qe += 1

nextq = []
nextqs, nextqe = 0, 0
while qs < qe:
    curx, cury = q[qs]    
    qs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

while nextqs < nextqe:
    curx, cury = nextq[nextqs]
    nextqs += 1

    for nx, ny in (curx-1, cury), (curx+1, cury), (curx, cury-1), (curx, cury+1):
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
            continue
        elif grid[nx][ny] == '#':
            continue
        elif grid[nx][ny] == 'S':
            ans = 1
            nextqs = nextqe
            break
        elif visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        nextq.append([nx, ny])
        nextqe += 1

if ans:
    print('Yes')
else:
    print('No')
