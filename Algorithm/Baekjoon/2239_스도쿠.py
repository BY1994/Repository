"""
2239 스도쿠

백트래킹
python3 시간초과
pypy3 통과
"""

# 현재 위치가 0 이면 그 값은 무조건 1~9 중 하나로 채워져야함. return 추가
sudoku = [[0 for i in range(9)] for j in range(9)]
count = 0
for i in range(9):
    oneline = input()
    for j in range(9):
        sudoku[i][j] = int(oneline[j])
        if sudoku[i][j] == 0:
            count += 1

flag = 0

def check(x, y, val):

    # row & col
    for i in range(9):
        if sudoku[i][y] == val or sudoku[x][i] == val:
            return 0

    # block
    startx = (x//3)*3
    starty = (y//3)*3
    for i in range(startx, startx+3):
        for j in range(starty, starty+3):
            if sudoku[i][j] == val:
                return 0
    return 1

def find(x, y, left):
    global flag

    if left == 0:
        flag = 1
        return

    for j in range(y+1, 9):
        if sudoku[x][j] == 0:
            for k in range(1, 10):
                if check(x, j, k):
                    sudoku[x][j] = k
                    find(x, j, left-1)
                    if flag == 1:
                        return
                    sudoku[x][j] = 0
            return

    for i in range(x+1, 9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if check(i, j, k):
                        sudoku[i][j] = k
                        find(i, j, left-1)
                        if flag == 1:
                            return
                        sudoku[i][j] = 0
                return

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            for k in range(1, 10):
                if check(i, j, k):
                    sudoku[i][j] = k
                    find(i, j, count-1)
                    if flag == 1:
                        break
            if flag == 1:
                break
    if flag == 1:
        break

for i in range(9):
    print(*sudoku[i], sep="")


# 너무 오래 걸리는 풀이
# 개선 필요
"""
sudoku = [[0 for i in range(9)] for j in range(9)]
count = 0
for i in range(9):
    oneline = input()
    for j in range(9):
        sudoku[i][j] = int(oneline[j])
        if sudoku[i][j] == 0:
            count += 1

flag = 0

def check(x, y, val):

    # row & col
    for i in range(9):
        if sudoku[i][y] == val or sudoku[x][i] == val:
            return 0

    # block
    startx = (x//3)*3
    starty = (y//3)*3
    for i in range(startx, startx+3):
        for j in range(starty, starty+3):
            if sudoku[i][j] == val:
                return 0
    return 1

def find(x, y, left):
    global flag

    if left == 0:
        flag = 1
        return

    for j in range(y+1, 9):
        if sudoku[x][j] == 0:
            for k in range(1, 10):
                if check(x, j, k):
                    sudoku[x][j] = k
                    find(x, j, left-1)
                    if flag == 1:
                        return
                    sudoku[x][j] = 0

    for i in range(x+1, 9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if check(i, j, k):
                        sudoku[i][j] = k
                        find(i, j, left-1)
                        if flag == 1:
                            return
                        sudoku[i][j] = 0

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            for k in range(1, 10):
                if check(i, j, k):
                    sudoku[i][j] = k
                    find(i, j, count-1)
                    if flag == 1:
                        break
                    sudoku[i][j] = 0
            if flag == 1:
                break
    if flag == 1:
        break

for i in range(9):
    print(*sudoku[i], sep="")
"""
