"""
12100 2048 (Easy)

2019.04.11 PBY 최초작성

반례
10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

답 1024

10
16 16 8 32 32 0 0 8 8 8
16 0 0 0 0 8 0 0 0 16
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

답 128

3
8 512 0
128 0 64
512 2 2

답 1024

3
0 16 0
16 512 0
512 256 1024

답 2048

"""

import copy


def combineBlock(board, depth, direction, curmax):
    global maxvalue, N
    # print(depth, direction, curmax)
    # for _ in range(N):
    #     print(board[_][:])

    if depth == 5: # 다섯번 이동했으면 끝
        if curmax > maxvalue:
            maxvalue = curmax
        return

    copied_board = copy.deepcopy(board)
    # 이동시켜서 변화시킨다음에
    # 시작점에서 끝점 돌면서 같은 수면 합치기
    if direction == 0: # 위로 밀었으면 위에서부터 합침
        for col in range(N):
            for row in range(N-1):
                if copied_board[row][col] == 0:
                    continue # 0부터는 시작하지 않는다
                nextrow = row+1
                check = 0 # 찾지 못함
                while True:
                    if nextrow >= N or nextrow < 0:
                        break
                    if copied_board[nextrow][col] > 0 and copied_board[row][col] != copied_board[nextrow][col]:
                        break # 합칠 수 없음
                    if copied_board[row][col] == copied_board[nextrow][col]:
                        check = 1
                        break
                    nextrow += 1
                if check == 1:
                    copied_board[row][col] *= 2
                    copied_board[nextrow][col] = 0 # 흡수
                    if copied_board[row][col] > curmax:
                        curmax = copied_board[row][col]

        # 하면서 curmax값 업데이트
    elif direction == 1: # 아래로 밀었으면 아래부터 합침
        for col in range(N):
            for row in range(N-1, 0, -1):
                if copied_board[row][col] == 0:
                    continue
                nextrow = row-1
                check = 0
                while True:
                    if nextrow < 0 or nextrow >= N:
                        break
                    if copied_board[nextrow][col] > 0 and copied_board[row][col] != copied_board[nextrow][col]:
                        break
                    if copied_board[row][col] == copied_board[nextrow][col]:
                        check = 1
                        break
                    nextrow -= 1
                if check == 1:
                    copied_board[row][col] *= 2
                    copied_board[nextrow][col] = 0
                    if copied_board[row][col] > curmax:
                        curmax = copied_board[row][col]

    elif direction == 2: # 왼쪽으로 민다
        for row in range(N):
            for col in range(N-1):
                if copied_board[row][col] == 0:
                    continue
                nextcol = col+1
                check = 0
                while True:
                    if 0 > nextcol or nextcol >= N:
                        break
                    if copied_board[row][nextcol] > 0 and copied_board[row][col] != copied_board[row][nextcol]:
                        break
                    if copied_board[row][col] == copied_board[row][nextcol]:
                        check = 1
                        break
                    nextcol += 1
                if check == 1:
                    copied_board[row][col] *= 2
                    copied_board[row][nextcol] = 0
                    if copied_board[row][col] > curmax:
                        curmax = copied_board[row][col]

    elif direction == 3:
        for row in range(N):
            for col in range(N-1, 0, -1):
                if copied_board[row][col] == 0:
                    continue
                nextcol = col - 1
                check = 0
                while True:
                    if 0 > nextcol or nextcol >= N:
                        break
                    if copied_board[row][nextcol] > 0 and copied_board[row][col] != copied_board[row][nextcol]:
                        break
                    if copied_board[row][col] == copied_board[row][nextcol]:
                        check = 1
                        break
                    nextcol -= 1
                if check == 1:
                    copied_board[row][col] *= 2
                    copied_board[row][nextcol] = 0
                    if copied_board[row][col] > curmax:
                        curmax = copied_board[row][col]

    # print("pull전에 상태")
    # for _ in range(N):
    #     print(copied_board[_][:])
    # # 0이 없도록 땡기기
    pullBlock(copied_board, direction)
    # print("pull후의 상태")
    # for _ in range(N):
    #     print(copied_board[_][:])
    # 상하좌우로 보냄
    combineBlock(copied_board, depth+1, 0, curmax)
    combineBlock(copied_board, depth+1, 1, curmax)
    combineBlock(copied_board, depth+1, 2, curmax)
    combineBlock(copied_board, depth+1, 3, curmax)

def pullBlock(board, direction):
    global N
    # direction 방향으로 가면서
    if direction == 0: # 위로 땡기기
        for col in range(N):
            for row in range(N):
                if board[row][col] != 0: # 숫자가 있으면 위로 땡기기
                    nextrow = row - 1
                    while True:
                        if 0 > nextrow or nextrow >= N:
                            break
                        if board[nextrow][col] != 0: # 0이 아닌 것을 만나면
                            break
                        nextrow -= 1
                    board[nextrow+1][col] = board[row][col]
                    if nextrow+1 != row:
                        board[row][col] = 0 # 0으로 그냥 바꿔버리니까 다 합쳐져버림....
    elif direction == 1: # 아래로 땡기기
        for col in range(N):
            for row in range(N-1, -1, -1):
                if board[row][col] != 0:
                    nextrow = row + 1
                    while True:
                        if 0 > nextrow or nextrow >= N:
                            break
                        if board[nextrow][col] != 0:
                            break
                        nextrow += 1
                    board[nextrow-1][col] = board[row][col]
                    if nextrow -1 != row:
                        board[row][col] = 0
    elif direction == 2: # 왼쪽으로 땡기기
        for row in range(N):
            for col in range(N):
                if board[row][col] != 0:
                    nextcol = col - 1
                    while True:
                        if 0 > nextcol or nextcol >= N:
                            break
                        if board[row][nextcol] != 0:
                            break
                        nextcol -= 1
                    board[row][nextcol+1] = board[row][col]
                    if nextcol+1 != col:
                        board[row][col] = 0
    elif direction == 3:
        for row in range(N):
            for col in range(N-1, -1, -1):
                if board[row][col] != 0:
                    nextcol = col + 1
                    while True:
                        if 0 > nextcol or nextcol >= N:
                            break
                        if board[row][nextcol] != 0:
                            break
                        nextcol += 1
                    board[row][nextcol-1] = board[row][col]
                    if nextcol -1 != col:
                        board[row][col] = 0



N = int(input())
board = []
maxvalue = 2
for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
    temp_max = max(temp)
    if maxvalue < temp_max:
        maxvalue = temp_max
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# 상하좌우로 보냄
combineBlock(board, 0, 0, maxvalue)
combineBlock(board, 0, 1, maxvalue)
combineBlock(board, 0, 2, maxvalue)
combineBlock(board, 0, 3, maxvalue)

print(maxvalue)

