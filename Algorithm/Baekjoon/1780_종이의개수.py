"""
1780 종이의 개수

재귀 연습
분할 정복
"""

import sys
input = sys.stdin.readline

paper = [] # 2187 = 3^7
ans = [0, 0, 0]

def recur(x, y, n):
    start = paper[x][y]
    flag = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != start:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        next_size = n//3
        recur(x, y, next_size)
        recur(x+next_size, y, next_size)
        recur(x+next_size*2, y, next_size)
        recur(x, y+next_size, next_size)
        recur(x, y+next_size*2, next_size)
        recur(x+next_size, y+next_size, next_size)
        recur(x+next_size*2, y+next_size, next_size)
        recur(x+next_size, y+next_size*2, next_size)
        recur(x+next_size*2, y+next_size*2, next_size)

    else:
        ans[start+1] += 1

N = int(input())
for i in range(N):
    paper.append(list(map(int, input().split())))

recur(0, 0, N)
print(ans[0], ans[1], ans[2], sep='\n')
