# Qualification Round 2019 - 2 You Can Go Your Own Way
# 2019.04.06 PBY
"""
input)
2
2
SE
5
EESSSESE
"""

# attempt 1 (5 points + Time Limit Exceeded)
"""
def go(x, y, direction):
    global ans
    if x == N-1 and y == N-1:
        ans = direction
        return
    # 2 direction
    if y + 1 < N and maze[x][y+1] != 'E':
        go(x, y+1, direction+'E')
    if x + 1 < N and maze[x+1][y] != 'S':
        go(x+1, y, direction+'S')
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Lydia = input()
    maze = [[0 for _ in range(N)] for __ in range(N)]
    L = [0,0]
    # Lydia's path check
    for i in range(len(Lydia)):
        if Lydia[i] == 'E':
            L[1] += 1 # east
            maze[L[0]][L[1]] = 'E'
        else:
            L[0] += 1 # south
            maze[L[0]][L[1]] = 'S'
    M = [0,0]
    ans = ''
    go(M[0], M[1], '')

    print("Case #{}: {}".format(tc, ans))
"""

# attempt 2 (5 Points + Runtime Error)
"""
def go(x, y, direction):
    global ans, flag
    if flag == 1:
        return
    if x == N-1 and y == N-1:
        ans = direction
        flag = 1
        return
    # 2 direction
    if y + 1 < N and maze[x][y+1] != 'E':
        go(x, y+1, direction+'E')
    if x + 1 < N and maze[x+1][y] != 'S':
        go(x+1, y, direction+'S')
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Lydia = input()
    maze = [[0 for _ in range(N)] for __ in range(N)]
    L = [0,0]
    # Lydia's path check
    for i in range(len(Lydia)):
        if Lydia[i] == 'E':
            L[1] += 1 # east
            maze[L[0]][L[1]] = 'E'
        else:
            L[0] += 1 # south
            maze[L[0]][L[1]] = 'S'
    M = [0,0]
    ans = ''
    flag = 0
    go(M[0], M[1], '')

    print("Case #{}: {}".format(tc, ans))
"""

# Attempt 3 (5 Points + Memory Limit Exceeded)
"""
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Lydia = input()
    maze = [[0 for _ in range(N)] for __ in range(N)]
    L = [0,0]
    # Lydia's path check
    for i in range(len(Lydia)):
        if Lydia[i] == 'E':
            L[1] += 1 # east
            maze[L[0]][L[1]] = 'E'
        else:
            L[0] += 1 # south
            maze[L[0]][L[1]] = 'S'
    M = [0,0]
    ans = ''
    q = deque([[M[0], M[1], '']])
    lenq = 1
    while q:
        for i in range(lenq):
            x, y, direction = q.popleft()
            if x == N-1 and y == N-1:
                ans = direction
                q = []
                break
            if y + 1 < N and maze[x][y+1] != 'E':
                q.append([x, y+1, direction+'E'])
            if x + 1 < N and maze[x+1][y] != 'S':
                q.append([x+1, y, direction+'S'])
        lenq = len(q)

    print("Case #{}: {}".format(tc, ans))
"""

# Attempt 4
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    direction = input()
    ans = ''
    for d in direction:
        if d == 'E':
            ans += 'S'
        else:
            ans += 'E'
    print("Case #{}: {}".format(tc, ans))
