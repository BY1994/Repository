"""
24725 엠비티아이
"""
import sys
input = sys.stdin.readline

MBTI = (('E', 'I'), ('N', 'S'), ('F','T'), ('P', 'J'))
direction = ((1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (-1, -1), (0, -1), (-1, 1))

def find_MBTI(x, y, depth, d):
    global N, M, ans

    if depth == 4:
        ans += 1
        return

    nx = x + direction[d][0]
    ny = y + direction[d][1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        return
    if board[nx][ny] in MBTI[depth]:
        find_MBTI(nx, ny, depth+1, d)

board = []
N, M = map(int, input().split())
for _ in range(N):
    board.append(input())

ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] in MBTI[0]:
            for d in range(8):
                find_MBTI(i, j, 1, d)

print(ans)
