"""
14948 군대탈출하기

BFS
처음에 잘못 생각해서 예제가 틀렸는데,
visited 를 단순 1, 0 체크하면 안 된다.
나중에 거길 방문했어도 더 이득인 경우가 있을 수 있기 때문에
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
army = []
for i in range(n):
    army.append(list(map(int, input().split())))

visited = [[[10000000000 for i in range(m)] for j in range(n)] for k in range(2)]
q = [[0, 0, army[0][0], 0]]
visited[0][0][0] = army[0][0]
qs = 0
qe = 1

ans = 10000000000

while qs < qe:
    x, y, level, used = q[qs]
    qs += 1
    
    if x == n-1 and y == m-1:
        ans = min(ans, level)
        continue

    # 장비 사용 x
    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        nextlevel = max(level, army[nx][ny])
        if visited[used][nx][ny] <= nextlevel:
            continue
        visited[used][nx][ny] = nextlevel
        q.append([nx, ny, nextlevel, used])
        qe += 1

    # 장비 사용 o
    if used == 0:
        for nx, ny in (x-2, y), (x+2, y), (x, y-2), (x, y+2):
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            nextlevel = max(level, army[nx][ny])
            if visited[1][nx][ny] <= nextlevel:
                continue
            visited[1][nx][ny] = nextlevel
            q.append([nx, ny, nextlevel, 1])
            qe += 1

print(ans)
