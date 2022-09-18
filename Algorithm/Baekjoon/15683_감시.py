"""
15683 감시

brute force

카메라의 최대 개수는 8개
4 방향으로 돌릴 수 있으므로 4**8 = 65536 개 brute force 만 하면 됨
여기에 map 을 돌면서 사각지대를 계산할 것이므로
65536 * 4 = 262144 만큼 돌 것으로 보인다.
(사각지대를 재귀 들어가면서 계산하고 싶었는데 방법이 없는 듯하다)

런타임 에러가 재귀 depth 때문이라고 생각했는데,
카메라 없는 경우 정말 index error 가 발생했다.

반례
카메라가 없는 경우 index error
3 3
6 6 6
6 6 6
0 6 6
"""

import sys
sys.setrecursionlimit(100000)

def recur(depth):
    global N, M, ans, camera_num, visited
    if depth == camera_num:
        for c in range(camera_num):
            # 각 방향별 보이면 진행
            for d in range(4):
                if CCTVdir[cameras[c][0]][cameras[c][3]][d]:
                    nx, ny = cameras[c][1], cameras[c][2]
                    while 0 <= nx < N and 0 <= ny < M:
                        if office[nx][ny] == 6: # 벽이면 못 감
                            break
                        if office[nx][ny] < 1 or office[nx][ny] > 6: # CCTV는 통과
                            office[nx][ny] = visited
                        nx = nx + directions[d][0]
                        ny = ny + directions[d][1]

        # 사각지대 계산
        value = 0
        for i in range(N):
            for j in range(M):
                if 1 <= office[i][j] <= 6:
                    continue
                elif office[i][j] == visited:
                    continue
                else:
                    value += 1

        ans = min(ans, value)
        visited += 1
        return

    for i in range(CCTVdir_num[cameras[depth][0]]):
        cameras[depth][3] = i
        recur(depth+1)
                    

# 상하좌우
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 카메라 종류, 회전한 방향, 각 방향 별 보이는지 여부
CCTVdir = (((0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0)),
           ((0, 0, 1, 1), (1, 1, 0, 0)),
           ((1, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0)),
           ((1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 0)),
           ((1, 1, 1, 1),))
CCTVdir_num = (4, 2, 4, 4, 1)

visited = 7

N, M = map(int, input().split())
ans = 0
office = []
for i in range(N):
    office.append(list(map(int, input().split())))

cameras = []
camera_num = 0
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cameras.append([office[i][j]-1, i, j, 0])
            camera_num += 1
        elif office[i][j] == 0:
            ans += 1

if camera_num > 0:
    for i in range(CCTVdir_num[cameras[0][0]]):
        cameras[0][3] = i
        recur(1)

print(ans)
