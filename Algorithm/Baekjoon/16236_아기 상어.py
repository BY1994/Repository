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

