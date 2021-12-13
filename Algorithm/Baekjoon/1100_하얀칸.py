"""
1100 하얀 칸
"""

ans = 0
for i in range(8):
    board = input()
    for j in range(8):
        if (i + j) % 2 == 0:
            if board[j] == 'F':
                ans += 1

print(ans)
