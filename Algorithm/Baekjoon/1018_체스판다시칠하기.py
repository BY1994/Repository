"""
1018 체스판 다시 칠하기
"""

def check(x, y):
    temp = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 ==0:
                if board[i][j] == 'B':
                    temp += 1
            else:
                if board[i][j] == 'W':
                    temp += 1
    return temp

board = []
N, M = map(int, input().split())
for _ in range(N):
    board.append(input())

min_ans = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        temp = check(i, j)
        min_ans = min(min_ans, temp, 64-temp)

print(min_ans)


# https://www.acmicpc.net/source/16449433
"""
import sys
from itertools import accumulate as acc
input = sys.stdin.readline
n, m = map(int, input().split())
y = [[0]*(m+1)]
for i in range(n):
    ac = [0]
    ac.extend(acc([((s=='W')+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    y.append([k + j for k, j in zip(ac, y[-1])])

res = 32
for i in range(n-7):
    for j in range(m-7):
        u = y[i+8][j+8]-y[i+8][j]-y[i][j+8]+y[i][j]
        res = min(res, u, 64-u)
print(res)
"""
