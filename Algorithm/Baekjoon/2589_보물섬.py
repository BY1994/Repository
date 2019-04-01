"""
보물섬

5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

2019.04.01 PBY 최초작성
"""

# BFS

#
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

