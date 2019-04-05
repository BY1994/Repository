"""BOJ"""
"""
13460_구슬 탈출 2

2019.04.05 PBY 최초작성
"""

from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().split())

# 초기 위치 잡아두기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j] # 공은 빼내고
            board[i][j] = '.' # 게임을 위한 세팅
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


# 이렇게 복잡하게 하드코딩할 필요가 없네! 둘이 동시에 움직이면 되니까!
"""
from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().split())

# 초기 위치 잡아두기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j] # 공은 빼내고
            board[i][j] = '.' # 게임을 위한 세팅
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
# 4 방향과 몇 번만에 왔는지를 넣어줌
# d가 0일 때 위로 옮길 때, B가 더 위에 있으면,
move = 0
def rollfunc(b1, b2, direction, move): # R, B 순서로 들어올 것
    if direction == 0:
        if b1[0] > b2[0]:
            # b2를 먼저 굴려준다.
            while board[b2[0]][b2[1]] == ".":
                b2[0] += dx[0] # 0 방향으로...
                b2[1] += dy[0]
            if board[b2[0]][b2[1]] == 'O':
                # R이 먼저 꺼내졌으면 성공!
                return 2
            while board[b1[0]][b1[1]] == "." and b2[0] != b1[0] and b2[1] != b1[1]: # 그 위치에 다른 구슬이 없어야함
                b1[0] += dx[0]
                b1[1] += dy[0]
            if board[b1[0]][b1[1]] != 'O':
                # 굴림이 끝남
                q.append([[b1[0]-dx[0], b1[1]-dy[0]], [b2[0]-dx[0], b2[1]-dy[0]], 0, move+1]) # 굴러간 방향 넣어주고

        else:
            # b1을 먼저 굴려준다.
            while board[b1[0]][b1[1]] == ".":  # 그 위치에 다른 구슬이 없어야함
                b1[0] += dx[0]
                b1[1] += dy[0]
            if board[b1[0]][b1[1]] == 'O':
                return 2

            while board[b2[0]][b2[1]] == "." and b2[0] != b1[0] and b2[1] != b1[1]:  # 그 위치에 다른 구슬이 없어야함
                b1[0] += dx[0]
                b1[1] += dy[0]
            if board[b2[0]][b2[1]] != 'O':
                # B가 먼저 꺼내졌으면 실패!
                q.append([[b1[0]-dx[0], b1[1]-dy[0]], [b2[0]-dx[0], b2[1]-dy[0]], 0, move+1])

    elif direction == 1: # 아래 방향이면
        if b1[0] < b2[0]:
            while board[b1[0]][b1[1]] == '.':
                b1[0]

    elif direction == 2: # 왼쪽 방향이면
    elif direction == 3: # 오른쪽 방향이면

rollfunc(R, B, 0)
rollfunc(R, B, 1)
rollfunc(R, B, 2)
rollfunc(R, B, 3)
"""
