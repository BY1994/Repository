"""
3085 사탕 게임

brute force

예제 2가...
사탕을 교환하지 않았을 때가 max임...

반례
https://www.acmicpc.net/board/view/58247
3
ZCY
ZCP
PYZ
답 2

교환하지 않아도 원래 맵에 최대 길이가 있는 경우,
이걸 고려하기 위해 같은 색이어도 무조건 교환하게 짰다
교환한 후에 가로선이나 세로선에 연속된 게 몇 개인지 찾도록 했다.
(교환한 거 고려해서 세는게 복잡해서 그냥 맵에서 교환해버렸다.)
"""

def count(startx, starty, endx, endy, value):
    ans = 0
    cur = 0
    for x in range(startx, endx):
        for y in range(starty, endy):
            if board[x][y] == value:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0
    ans = max(ans, cur)

    return ans

N = int(input())
board = []
for i in range(N):
    board.append(list(input()))

ans = 0
for i in range(N):
    for j in range(N):
        # 교환
        for nx, ny in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

            # 상하
            ans = max(ans, count(0, j, N, j+1, board[i][j]))
            # 좌우
            ans = max(ans, count(i, 0, i+1, N, board[i][j]))

            board[i][j], board[nx][ny] = board[nx][ny], board[i][j]

print(ans)

# 예제 2가 답이 안 나옴...
# 사탕을 무조건 교환해야한다고 생각했으니까...
"""
def count(startx, starty, endx, endy, value):
    cur = 1
    for x in range(startx, endx):
        for y in range(starty, endy):
            if board[x][y] == value:
                cur += 1
    return cur

N = int(input())
board = []
for i in range(N):
    board.append(input())

ans = 0
for i in range(N):
    for j in range(N):
        for nx, ny in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[i][j] == board[nx][ny]:
                continue

            # 상
            ans = max(ans, count(0, j, i, j+1, board[nx][ny]))
            # 하
            ans = max(ans, count(i+1, j, N, j+1, board[nx][ny]))
            # 좌
            ans = max(ans, count(i, 0, i+1, j, board[nx][ny]))
            # 우
            ans = max(ans, count(i, j+1, i+1, N, board[nx][ny]))

print(ans)
"""

# 예제 1 틀림
# 상하좌우 다 합이 아니라 한 방향으로만
"""
N = int(input())
board = []
for i in range(N):
    board.append(input())

ans = 0
for i in range(N):
    for j in range(N):
        for nx, ny in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if board[i][j] == board[nx][ny]:
                continue
            
            cur = 1
            # 상
            for c in range(i-1, -1, -1):
                if board[c][j] == board[nx][ny]:
                    cur += 1
            # 하
            for c in range(i+1, N):
                if board[c][j] == board[nx][ny]:
                    cur += 1
            # 좌
            for c in range(j-1, -1, -1):
                if board[i][c] == board[nx][ny]:
                    cur += 1
            # 우
            for c in range(j+1, N):
                if board[i][c] == board[nx][ny]:
                    cur += 1

            ans = max(ans, cur)

print(ans)
"""
