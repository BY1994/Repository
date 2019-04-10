"""
16236 아기 상어

2019.04.09 PBY 최초작성


# 모든 물고기를 항상 다 먹을 수 있는 건 아닙니다. (https://www.acmicpc.net/board/view/31476)
2
9 3
3 1

# 상어의 크기가 9까지 커진 이후 올바르게 판단을 하지 못하고 무한루프(https://www.acmicpc.net/board/view/35531)
10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 9

# 내 코드 틀린 부분 => 장애물이 있어서 못 가는 경우를 모름
3
0 4 1
0 0 4
0 9 0

"""

# 더 간단하게 짜본 코드
from collections import deque

def findFish(x, y, size):
    global N
    # 모든 위치 별로 거리를 다 저장할 것
    dist = [[401 for _ in range(N)] for __ in range(N)]
    dist[x][y] = 0 # 처음 내 거리는 0
    q = deque([[x, y]])
    lenq = len(q)
    while q:
        for i in range(lenq):
            nextx, nexty = q.popleft()
            for d in range(4):
                if 0 <= nextx+dx[d] < N and 0 <= nexty+dy[d] < N:
                    if dist[nextx+dx[d]][nexty+dy[d]] == 401: # 아직 방문 안함
                        if sea[nextx+dx[d]][nexty+dy[d]] <= size:
                            dist[nextx+dx[d]][nexty+dy[d]] = dist[nextx][nexty] + 1
                            q.append([nextx+dx[d], nexty+dy[d]])
        lenq = len(q)

    # 큐를 다 돌고 나면 모든 지점의 거리가 정해진다.
    mindist = 401
    check = 0
    for i in range(N):
        for j in range(N):
            if dist[i][j] < mindist and 0 < sea[i][j] < size: # 그냥 빈 공간인지 내가 먹을 수 있는 물고기인지 확인
                check = 1
                mindist = dist[i][j]
                minindex = [i, j, mindist]

    if check == 0:
        return False
    else:
        return minindex



N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))

# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            me = [i, j]
            sea[i][j] = 0 # 상어 빼내기

t = 0
size = 2
eat = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    fish = findFish(me[0], me[1], size)
    if fish == False:
        break
    me[0] = fish[0]; me[1] = fish[1]
    sea[fish[0]][fish[1]] = 0 # 물고기 사라짐
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    t += fish[2]

print(t)





# 통과는 했으나 시간이 제일 느렸다.
"""
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def distance(x, y, i, j, size):
    global N
    visited = [[0 for _ in range(N)] for __ in range(N)]
    q = deque([[x, y]])
    visited[x][y] = 1
    lenq = len(q)
    di = 0
    check = 0
    while q:
        for _ in range(lenq):
            nextx, nexty = q.popleft()
            # visited[nextx][nexty] = 1  # 간 길로 표시
            if nextx == i and nexty == j:
                check = 1
                q = []
                break
            for d in range(4):
                if 0 <= nextx + dx[d] < N and 0 <= nexty + dy[d] < N:
                    if sea[nextx + dx[d]][nexty + dy[d]] <= size and visited[nextx + dx[d]][nexty + dy[d]] == 0:  # 아직 방문 안 했을 때
                        q.append([nextx + dx[d], nexty + dy[d]])
                        # visit을 여러번 하는 것 같다....
                        visited[nextx+dx[d]][nexty+dy[d]] = 1 # 방문 표시를 미리 해버리기

        lenq = len(q)
        di += 1

    if check == 0:
        return False
    else:
        return di -1
#    return max(0, di-1) # 내 큐가 도는 방식 때문에 거리가 하나 더 추가된 걸로 계산이 된다.


def nextlocation(x, y, size):
    global N
    check = 0
    mind = N * N
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size:
                temp = distance(x, y, i, j, size)
                if temp == False:
                    continue
                if mind > temp:
                    check = 1
                    mind = temp
                    nextl = [i, j, mind]

    if check == 0:
        return False
    else:
        return nextl




N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))

# find my location
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            me = [i, j] # 내가 날 먹나보다...헐......
            sea[i][j] = 99999

# my location to other location
possible = 1 # 가능하다고 가정
t = 0
size = 2
eat = 0
while possible == 1:
    # 찾을 수 없으면 0을 출력한다.
    nextl = nextlocation(me[0], me[1], size)
    if nextl == False:
        possible = 0
        break
    sea[me[0]][me[1]] = 0 # 갈 수 있는 길로 대체
    me[0] = nextl[0]
    me[1] = nextl[1]
    sea[me[0]][me[1]] = 99999
    eat += 1
    if eat == size:
        size += 1 # 몸 크기가 하나 커짐
        eat = 0 # 먹은 것 초기화
    t += nextl[2] # 시간이 하나씩이 아니라!!!  거리만큼 흘러감!!!

print(t)

"""