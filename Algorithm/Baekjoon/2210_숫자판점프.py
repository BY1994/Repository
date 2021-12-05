"""
2210 숫자판 점프
"""

def dfs(x, y, cur, depth):
    if depth == 6:
        ans.append(cur)
        return
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        if x + dx < 5 and y + dy < 5 and x+dx >= 0 and y + dy >= 0:
            dfs(x+dx, y+dy,cur*10 + pan[x+dx][y+dy] ,depth+1)
            

pan = []
ans = []
for _ in range(5):
    pan.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, pan[i][j], 1)

print(len(set(ans)))
