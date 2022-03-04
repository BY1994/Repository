"""
2580 스도쿠

백트래킹

N과 M 문제와 달리 원본을 수정하는데, 원본을 참조함
그래서 원본을 수정하고 나면 반드시 0 으로 돌려줘야함
"""

import sys
input = sys.stdin.readline

def check(x, y, value):
    for i in range(9):
        if sudoku[i][y] == value:
            return False
        if sudoku[x][i] == value:
            return False
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3+3):
            if sudoku[i][j] == value:
                return False
    return True

def backtracking(x, y, number, depth):
    global flag, p_num
    if flag == 1:
        return
    if depth >= p_num:
        for i in range(9):
            print(*sudoku[i])
        flag = 1
        return
    nextx = problem[depth][0]
    nexty = problem[depth][1]
    for i in range(1, 10):
        if check(nextx, nexty, i):
            sudoku[nextx][nexty] = i
            backtracking(nextx, nexty, i, depth+1)
            sudoku[nextx][nexty] = 0

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

problem = []
p_num = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            problem.append((i, j))
            p_num += 1

flag = 0
x = problem[0][0]
y = problem[0][1]

for i in range(1, 10):
    if flag == 1:
        break
    if check(x, y, i):
        sudoku[x][y] = i
        backtracking(x, y, i, 1)
        sudoku[x][y] = 0
