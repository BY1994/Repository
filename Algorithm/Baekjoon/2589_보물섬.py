"""
보물섬

5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

BFS, Brute Force

2019.04.01 PBY 최초작성 (미완성)
2022.07.19 PBY 통과
"""

# 2022.07.19 통과

N, M = map(int, input().split())
mintime = 0
mymap = []
for i in range(N):
    mymap.append(input())

visited = [[0 for i in range(M)] for j in range(N)]
visit_check = 0

for sx in range(N):
    for sy in range(M):
        if mymap[sx][sy] == 'W':
            continue
        visit_check += 1
        q = [[sx, sy, 0]]
        qs = 0
        qe = 1
        visited[sx][sy] = visit_check

        while qs < qe:
            x, y, dist = q[qs]
            qs += 1

            mintime = max(mintime, dist)

            for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if mymap[nx][ny] == 'W':
                    continue
                if visited[nx][ny] == visit_check:
                    continue
                visited[nx][ny] = visit_check
                q.append([nx, ny, dist+1])
                qe += 1

print(mintime)

# 2019.04.01 작성본 (미완성)
# BFS
import copy
from collections import deque

row, col = map(int, input().split())
island = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    temp = input()
    for j in range(col):
        if temp[j] == 'L':
            island[i][j] = 0
        else:
            island[i][j] = 1
islandcopy = copy.deepcopy(island)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# L을 찾아서, 거기서 갈 수 있는 최대 먼 곳을 잡음
def findmostfar(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        flag = 0
        for d in range(4):
            if 0 <= x + dx[d] < row and 0 <= y + dy[d] < col:  # 판을 넘어서지 않고
                # 그곳이 육지일 때
                if islandcopy[x + dx[d]][y + dy[d]] == 0:
                    flag = 1
                    islandcopy[x + dx[d]][y + dy[d]] = islandcopy[x][y] + 1
                    q.append([x + dx[d], y + dy[d]])
        if flag == 0:
            # 다음 길이 없으니까 distance에 넣기
            distance.append(islandcopy[x][y])
    return x, y


# 최대 먼 곳 하나씩 찾아두기
for i in range(row):
    for j in range(col):
        if islandcopy[i][j] == 0:
            distance = []
            islandcopy[i][j] = 1
            x, y = findmostfar(i, j) # 해당 육지에서 제일 먼 곳이 distance에 들어감


"""
# 한방에 끝내려고 욕심 부렸는데, 아닌 것 같다.
import copy
from collections import deque

row, col = map(int, input().split())
island = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    temp = input()
    for j in range(col):
        if temp[j] == 'L':
            island[i][j] = 0
        else:
            island[i][j] = 1
islandcopy = copy.deepcopy(island)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# L을 찾아서, 거기서 갈 수 있는 최대 먼 곳을 잡음
def findmostfar(x, y):
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        flag = 0
        for d in range(4):
            if 0<=x + dx[d]<row and 0<=y+dy[d]<col: # 판을 넘어서지 않고
                # 그곳이 육지일 때
                if islandcopy[x+dx[d]][y+dy[d]] == 0:
                    flag = 1
                    islandcopy[x+dx[d]][y+dy[d]] = islandcopy[x][y] + 1
                    q.append([x+dx[d],y+dy[d]])
        if flag == 0:
            # 다음 길이 없으니까 distance에 넣기
            distance.append(islandcopy[x][y])
    return x, y
    

# 최대 먼 곳 하나씩 찾아두기
for i in range(row):
    for j in range(col):
        if islandcopy[i][j] == 0:
            distance = []
            islandcopy[i][j] = 1
            x, y = findmostfar(i, j)
            distance.sort()
            print(distance[-1]+distance[-2])

# 먼 곳에서 가장 먼 곳까지의 거리
# distance의 제일 긴 곳
"""


