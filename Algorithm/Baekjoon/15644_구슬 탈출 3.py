"""
반례
https://boohyunsik.github.io/exit-marble-test-case/
5 7
#######
#.B...#
#..O#.#
#...R.#
#######
3

직접 만든 반례
4 5
#####
#B.R#
#.O.#
#####
2


10 8
########
#.##O#.#
##.....#
#..#.#.#
##....##
#...#..#
#......#
#...#..#
#..RB..#
########

5 9
#########
#.#.#.#.#
#.R.#.B.#
####O####
#########
=> 내 문제는 둘이 멀리 떨어져있는데, 굴러와서 같은 자리로 만난 경우, 자리 조정에 실패하는 것이었다.
"""


def beadRolling(x1, y1, x2, y2, curd, directions, depth):
    global N, M, possible, ans, minvalue
    print("방향", curd, "현재까지", directions, "이동수", depth)
    print(visited)
    if depth >= minvalue: # 이미 필요한 것보다 더 돌았으면
        return

    origin = [x1, y1, x2, y2]

    # if depth == 10: # 1~3 번 문제를 위한 조건
    #     return

    Rpole = 0; Bpole = 0 # 여기가 실수로 1이 되어있었다.
    check1 = 0; check2 = 0
    while True:
        # 그 방향으로 빼줌
        if 0 <= x1+dx[curd] < N and 0 <= y1+dy[curd] < M and board[x1 + dx[curd]][y1 + dy[curd]] != "#":
            if board[x1+dx[curd]][y1+dy[curd]] == 'O': # 구멍을 만나면 끝!
                Rpole = 1
                check1 = 1
            else:
                x1 += dx[curd]
                y1 += dy[curd]
        else:
            check1 = 1

        if 0 <= x2+dx[curd] < N and 0 <= y2+dy[curd] < M and board[x2+dx[curd]][y2+dy[curd]] != '#':
            if board[x2+dx[curd]][y2+dy[curd]] == 'O':
                Bpole = 1
                check2 = 1
            else:
                x2 += dx[curd]
                y2 += dy[curd]
        else:
            check2 = 1

        if check1 == 1 and check2 == 1: # 둘다 더 이상 안 움직이면
            break

    if Bpole == 1: # 구멍에 들어가면 안 되는 애가 들어감
        return
    if Rpole == 1: # 내가 성공하면!
        possible = 1
        if minvalue > depth + 1:
            minvalue = depth + 1
            ans = directions
        return

    # 다음 길로 넘기는데,
    # 둘 중에 더 앞선 애가 앞에 있도록 뒤에 있는 애의 위치 조정
    if x1==x2 and y1==y2: # 둘이 같은 위치여선 안 된다.
        if curd == 0: # 위 방향이면
            if origin[0] < origin[2]: # x1보다 x2가 더 아래에 있으면
                x2 += 1 # 아래로 옮기기
            else:
                x1 += 1
        elif curd == 1: # 아래로 옮기면
            if origin[0] < origin[2]: # x2가 더 아래에 있으면
                x1 -= 1 # x1을 위로 옮기기
            else:
                x2 -= 1
        elif curd == 2: # 왼쪽으로 옮길 때
            if origin[1] < origin[3]: # y2가 더 오른쪽에 있으면
                y2 += 1 # y2를 오른쪽으로 옮기기
            else:
                y1 += 1
        elif curd == 3: # 오른쪽으로 옮길 때
            if origin[1] < origin[3]: # y2가 더 오른쪽에 있으면
                y1 -= 1
            else:
                y2 -= 1

    # if [x1, y1, x2, y2] in visited:
    #     return
    # else:
    #     visited.append([x1, y1, x2, y2])
    if visited.get((x1, y1, x2, y2)) == 1:
        return # 이미 방문했으면 더 처리하지 않음
    else:
        visited[(x1, y1, x2, y2)] = 1 # 딕셔너리에 넣어줌

    # if origin[0] + dx[curd] == origin[2] and origin[1] + dy[curd] == origin[3]: #
    #     x1 -= dx[curd]; y1 -= dy[curd]
    # elif origin[2] + dx[curd] == origin[0] and origin[3] + dy[curd] == origin[1]:
    #     x2 -= dx[curd]; y2 -= dy[curd]


    # 다음 함수
    beadRolling(x1, y1, x2, y2, 0, directions+'U', depth+1)
    beadRolling(x1, y1, x2, y2, 1, directions+'D', depth+1)
    beadRolling(x1, y1, x2, y2, 2, directions+'L', depth+1)
    beadRolling(x1, y1, x2, y2, 3, directions+'R', depth+1)

    # visited.pop(-1)
    visited.pop((x1, y1, x2, y2))

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j]
        elif board[i][j] == 'B':
            B = [i, j]

# R, B 위치를 찾음
# 4 방향으로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

minvalue = 0xffffff
possible = 0
ans = ''

visited = {(R[0], R[1], B[0], B[1]):1} # timebird님 추천!
# visited = []
beadRolling(R[0], R[1], B[0], B[1], 0, 'U', 0)
beadRolling(R[0], R[1], B[0], B[1], 1, 'D', 0)
beadRolling(R[0], R[1], B[0], B[1], 2, 'L', 0)
beadRolling(R[0], R[1], B[0], B[1], 3, 'R', 0)

if possible == 0:
    # print(0) # 1번용
    print(-1) # 2, 3번용
else:
    # print(1) # 1번용
    print(minvalue)
    print(ans) # 3번용




"""
import copy


def moveBeady(x, y, state, direct, copy_board):
    returnstate = 0
    while True:
        if 0 > y or y >= M or 0 > x or x >= M:
            break  # 불가능한 지점이면 꺼냄
        if copy_board[x][y] == 'O':
            returnstate = state  # 1이면 먼저 들어가서 성공
            break
        if copy_board[x][y] == '#':
            break
        y += direct
    return x, y - direct, returnstate

def moveBeadx(x, y, state, direct, copy_board):
    returnstate = 0
    while True:
        if 0 > y or y >= M or 0 > x or x >= M:
            break  # 불가능한 지점이면 꺼냄
        if copy_board[x][y] == 'O':
            returnstate = state  # 1이면 먼저 들어가서 성공
            break
        if copy_board[x][y] == '#':
            break
        x += direct
    return x - direct, y, returnstate


def beadRolling(board, depth, directions, R0, R1, B0, B1):
    global N, M, minvalue, ans
    if depth > minvalue: # 가지치기
        return
    # print("함수 불리면", directions)
    # for _ in range(N):
    #     print(board[_][:])
    copy_board = copy.deepcopy(board)

    state = 0 # 0 이면 그냥 구슬 굴러감 1이면 빨간 구슬 먼저 들어가 성공 2면 파란 구슬 먼저 들어가 실패
    if depth == 10:
        return # 더 움직이지 않는다
    if directions[-1] == 'L': # 왼쪽으로 옮기라고 하면
        # 더 먼저 있는 애를 먼저 왼쪽으로 옮겨줌
        if R1 < B1:
            x = R0; y = R1-1
            x, y, state = moveBeady(x, y, 1, -1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

            x = B0; y = B1-1
            x, y, state = moveBeady(x, y, 2, -1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

        else:
            x = B0; y = B1-1
            x, y, state = moveBeady(x, y, 2, -1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

            x = R0; y = R1-1
            x, y, state = moveBeady(x, y, 1, -1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

        if state == 1:  # 성공
            if minvalue > depth + 1:
                minvalue = depth + 1
                ans = directions
            return

    elif directions[-1] == 'R': # 오른쪽으로 이동
        if R1 > B1: # 더 오른쪽에 있으면 먼저 이동
            x = R0; y = R1+1
            x, y, state = moveBeady(x, y, 1, 1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

            x = B0; y = B1+1
            x, y, state = moveBeady(x, y, 2, 1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return
        else:
            x = B0; y = B1 + 1
            x, y, state = moveBeady(x, y, 2, 1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

            x = R0; y = R1 + 1
            x, y, state = moveBeady(x, y, 1, 1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

        if state == 1:
            if minvalue > depth + 1:
                minvalue = depth + 1
                ans = directions
            return

    elif directions[-1] =='U':
        if R0 < B0: # 더 위에 있으면 먼저 이동
            x = R0 - 1; y = R1
            x, y, state = moveBeadx(x, y, 1, -1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

            x = B0 - 1; y = B1
            x, y, state = moveBeadx(x, y, 2, -1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

        else:
            x = B0 - 1; y = B1
            x, y, state = moveBeadx(x, y, 2, -1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

            x = R0 - 1; y = R1
            x, y, state = moveBeadx(x, y, 1, -1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y
        if state == 1:
            if minvalue > depth + 1:
                minvalue = depth + 1
                ans = directions
            return

    elif directions[-1] == 'D': # 아래로 이동
        if R0 > B0: # 더 아래에 있으면
            x = R0 + 1; y = R1
            x, y, state = moveBeadx(x, y, 1, 1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

            x = B0 + 1; y = B1
            x, y, state = moveBeadx(x, y, 2, 1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

        else:
            x = B0 + 1; y = B1
            x, y, state = moveBeadx(x, y, 2, 1, copy_board)
            copy_board[B0][B1] = '.'
            copy_board[x][y] = 'B'
            B0 = x; B1 = y
            if state == 2:
                return

            x = R0 + 1; y = R1
            x, y, state = moveBeadx(x, y, 1, 1, copy_board)
            copy_board[R0][R1] = '.'
            copy_board[x][y] = 'R'
            R0 = x; R1 = y

        if state == 1:
            if minvalue > depth + 1:
                minvalue = depth + 1
                ans = directions
            return

    beadRolling(copy_board, depth+1, directions+'L', R0, R1, B0, B1)
    beadRolling(copy_board, depth+1, directions+'R', R0, R1, B0, B1)
    beadRolling(copy_board, depth+1, directions+'U', R0, R1, B0, B1)
    beadRolling(copy_board, depth+1, directions+'D', R0, R1, B0, B1)



N, M = map(int, input().split())
board = [[[] for _ in range(M)] for __ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        board[i][j] = temp[j]
        if temp[j] == 'R':
            R = [i, j] #  꺼내야하는 구슬
        elif temp[j] == 'B':
            B = [i, j]

minvalue = 101
ans = ''

beadRolling(board, 0, 'L', R[0], R[1], B[0], B[1])
beadRolling(board, 0, 'R', R[0], R[1], B[0], B[1])
beadRolling(board, 0, 'U', R[0], R[1], B[0], B[1])
beadRolling(board, 0, 'D', R[0], R[1], B[0], B[1])

if minvalue == 101:
    print(-1)
else:
    print(minvalue)
    print(ans)

"""