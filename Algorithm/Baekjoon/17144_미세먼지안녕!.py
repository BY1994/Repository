"""
17144 미세먼지 안녕

BFS가 아니라 시뮬레이션

개선점
먼지량 보존의 법칙
https://www.acmicpc.net/board/view/55267
공기청정기에 들어간 먼지량만 빼주면 총량
"""


R, C, T = map(int, input().split())
map1 = []
cleaner = -1

for i in range(R):
    map1.append(list(map(int, input().split())))
    if cleaner < 0 and map1[i][0] == -1:
        cleaner = i

map2 = [[0 for i in range(C)] for j in range(R)]

while T > 0:
    # 1. 확산
    for i in range(R):
        for j in range(C):
            map2[i][j] = 0
    for i in range(R):
        for j in range(C):
            value = map1[i][j]
            if value > 0:
                for nextx, nexty in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if nextx < 0 or nextx >= R or nexty < 0 or nexty >= C:
                        continue
                    if map1[nextx][nexty] == -1: # 이거 없으면 답 187 출력함
                        continue
                    map2[nextx][nexty] += value // 5
                    map1[i][j] -= value // 5
            map2[i][j] += map1[i][j]

    # 2. 공기청정기
    for i in range(cleaner-1): # 바로 위 값은 공기청정기에 들어가서 없어짐
        map1[i+1][0] = map2[i][0]
    for i in range(C-1):
        map1[0][i] = map2[0][i+1]
    for i in range(cleaner):
        map1[i][C-1] = map2[i+1][C-1]
    for i in range(C-2, 0,-1): # 공기 청정기에서 나오는 거는 0
        map1[cleaner][i+1] = map2[cleaner][i]
    map1[cleaner][1] = 0

    # 바람 안 닿는 영역
    for i in range(1, cleaner):
        for j in range(1, C-1):
            map1[i][j] = map2[i][j]

    for i in range(cleaner+2, R-1): # 바로 아래 값은 공기청정기에 들어가서 없어짐
        map1[i][0] = map2[i+1][0]
    for i in range(C-1):
        map1[R-1][i] = map2[R-1][i+1]
    for i in range(R-2, cleaner, -1):
        map1[i+1][C-1] = map2[i][C-1]
    for i in range(C-2, 0, -1):
        map1[cleaner+1][i+1] = map2[cleaner+1][i]
    map1[cleaner+1][1] = 0

    # 바람 안 닿는 영역
    for i in range(cleaner+2, R-1):
        for j in range(1, C-1):
            map1[i][j] = map2[i][j]

    T -= 1

total = 2 # 공기 청정기 -1 -1
for i in range(R):
    for j in range(C):
        total += map1[i][j]

print(total)
