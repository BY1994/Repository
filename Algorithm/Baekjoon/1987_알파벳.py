"""
1987 알파벳

백트래킹
https://dirmathfl.tistory.com/162
https://campkim.tistory.com/18

22/05/04
메모리 초과
단순히 BFS 에 방문한 알파벳을 비트로 체크하면 구현할 수 있다고 생각했는데,
위의 블로그나 질문 게시판을 보듯 이렇게 풀면 시간초과 혹은 메모리 초과가 난다.

양 방향으로 뻗어나갔다고 할 때 둘이 만나는 지점이 있으면 다시 방문했던 곳을 또 방문하는 현상이 생긴다.
그거 때문에 메모리 초과가 발생했을 것으로 보인다.
BFS 로 못 푸는 문제인가?

22/06/12
DFS 로 변경 -> 통과

BFS 풀이도 가능
visited 배열 크기를 반드시 3차원으로 잡으려고 할 필요는 없었다.
vis[ny][nx] ^ (cur|num(ny, nx) 로 체크하면 가능
https://www.acmicpc.net/source/40196383

20 x 20 크기였기 때문에 재귀 limit 에 걸리지 않았음
"""

def dfs(x, y, dist, alpha):
    global ans, R, C

    ans = max(dist, ans)

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if visited[nx][ny] == 1:
            continue
        if (alpha >> (ord(board[nx][ny])-A)) & 1:
            continue

        newalpha = alpha | (1 << (ord(board[nx][ny])-A))
        visited[nx][ny] = 1
        dfs(nx, ny, dist+1, newalpha)
        visited[nx][ny] = 0

R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(input())

visited = [[0 for i in range(20)] for j in range(20)]

ans = 1
A = ord('A')
visited[0][0] = 1
dfs(0, 0, 1, 1 <<(ord(board[0][0])-A))
print(ans)

# visited 배열이 너무 큼
# 실행 안 됨
"""
R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(input())

visited = [[[0 for i in range(1<<26)] for j in range(20)] for k in range(20)]

ans = 1
A = ord('A')
q = [[0, 0, 1 <<(ord(board[0][0])-A),1]]
qs = 0
qe = 1
visited[0][0][1 <<(ord(board[0][0])-A)] = 1

while qs < qe:
    x, y, alpha, dist = q[qs]
    qs += 1
    ans = max(ans, dist)

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if visited[nx][ny][alpha] == 1:
            continue
        if (alpha >> (ord(board[nx][ny])-A)) & 1:
            continue
        newalpha = alpha | (1 << (ord(board[nx][ny])-A))
        q.append([nx, ny, newalpha, dist+1])
        visited[nx][ny][newalpha] = 1
        qe += 1
print(ans)
"""

# 그냥 visited 체크 추가는 예제도 틀림
"""
R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(input())

ans = 1
A = ord('A')
q = [[0, 0, 1 << (ord(board[0][0])-A),1]]
visited = [[0 for i in range(C)] for j in range(R)]
visited[0][0] = 1
qs = 0
qe = 1
while qs < qe:
    x, y, alpha, dist = q[qs]
    qs += 1
    ans = max(ans, dist)

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if (alpha >> (ord(board[nx][ny])-A)) & 1:
            continue
        if visited[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        q.append([nx, ny, alpha | (1 << (ord(board[nx][ny])-A)), dist+1])
        qe += 1
print(ans)
"""

# 메모리 초과
"""
R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(input())

ans = 1
A = ord('A')
q = [[0, 0, 1 <<(ord(board[0][0])-A),1]]
qs = 0
qe = 1
while qs < qe:
    x, y, alpha, dist = q[qs]
    qs += 1
    ans = max(ans, dist)

    for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if (alpha >> (ord(board[nx][ny])-A)) & 1:
            continue
        q.append([nx, ny, alpha | (1 << (ord(board[nx][ny])-A)), dist+1])
        qe += 1
print(ans)
"""
