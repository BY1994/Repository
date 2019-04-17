"""
16918 봄버맨

2019.04.17 PBY 최초작성
"""

R, C, N = map(int, input().split())
board = [[] for _ in range(R)]
for i in range(R):
    temp = input()
    for j in range(C):
        if temp[j] == 'O':
            board[i].append(1) # 1 이상은 폭탄이 설치된 시간 1초 동안 봄버맨은 아무것도 하지 않는다. 시간이 2로 흘러감
        else:
            board[i].append(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 격자판의 상태 출력
t = 0
while t < N:

    # 시간이 흐르고
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                board[i][j] += 1
    t += 1
    if t == N:
        break

    # 없는 부분을 다시 폭탄으로 채운다
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                board[i][j] = 1


    # 시간이 흐르고
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                board[i][j] += 1

    t += 1
    if t == N:
        break

    # 폭탄 터뜨림
    for i in range(R):
        for j in range(C):
            if board[i][j] >= 3: # 3초가 되면 폭발
                for d in range(4):
                    if 0 <= i+dx[d] < R and 0 <= j+dy[d] < C and board[i+dx[d]][j+dy[d]] < 3:
                        board[i+dx[d]][j+dy[d]] = 0 # 없애버림
                board[i][j] = 0 # 내 자리도 터져야함

# 출력
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            board[i][j] = 'O'
        else:
            board[i][j] = '.'
    print(''.join(board[i]))