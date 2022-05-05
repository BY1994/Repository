"""
17143 낚시왕

2019.04.17 PBY 최초작성
2022.05.05 PBY 새로 문제 풀이
"""

# 시간초과 해결하기
# (1) 상어 없애는 거 -1 표시가 아니라 뒤에서 가져와서 채우는 걸로
# (2) 상어 다음 위치 계산할 때 조금이라도 더 빨리 계산하려고 로직 개선
# => (1), (2) 안 하고 pypy3 로 제출해서 통과함 

# 틀린 부분 발견. 아래 조건 안 넣었었음 (예제에서 안 걸림)
# 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

# => 틀렸습니다
# 크기가 작아서 잡아먹힌 상어를 -1 처리 안 해줌

# => 틀렸습니다
# 크기가 큰 상어입장만 처리해주고
# 작은 상어가 for 문 대상일 때 처리 안 해줌. else 문 추가

R, C, M = map(int, input().split())
board = [[0 for i in range(C)] for j in range(R)]
shark = [0]*(M+1)
snum = 1
ans = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[snum] = [r-1, c-1, s, d-1, z]
    board[r-1][c-1] = snum
    snum += 1

# 1 위 2 아래 3 오른쪽 4 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
reverse = [1, 0, 3, 2]

for fisher in range(C):
    # C열의 상어 잡기
    for i in range(R):
        if board[i][fisher]:
            ans += shark[board[i][fisher]][4]
            shark[board[i][fisher]] = -1
            board[i][fisher] = 0
            break

    # 상어 위치 업데이트
    for s in range(1,M+1):
        if shark[s] == -1:
            continue

        x, y, d = shark[s][0], shark[s][1], shark[s][3]
        if d == 0 or d == 1:
            remain = shark[s][2] % ((R-1)*2)
        else:
            remain = shark[s][2] % ((C-1)*2)
        board[x][y] = 0

        while remain:
            # 그 방향으로 이동
            nx, ny = x+dx[d], y+dy[d]
            if nx >= R:
                nx = R-2
                d = reverse[d]

            elif nx < 0:
                nx = 1
                d = reverse[d]

            if ny >= C:
                ny = C-2
                d = reverse[d]

            elif ny < 0:
                ny = 1
                d = reverse[d]

            remain -= 1
            x, y = nx, ny

        shark[s][0] = x
        shark[s][1] = y
        shark[s][3] = d

    # 큰 상어가 다른 상어 잡아먹음
    for s in range(1, M+1):
        if shark[s] == -1:
            continue
        x, y = shark[s][0], shark[s][1]
        if board[x][y]:
            if shark[board[x][y]][4] < shark[s][4]:
                # 잡아먹힌 거 업데이트
                shark[board[x][y]] = -1
                board[x][y] = s
            else:
                # 작은 거면 이게 잡아먹힘
                shark[s] = -1
        else:
            board[x][y] = s

print(ans)

# 시간초과
"""
R, C, M = map(int, input().split())
board = [[0 for i in range(C)] for j in range(R)]
shark = [0]*(M+1)
snum = 1
ans = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[snum] = [r-1, c-1, s, d-1, z]
    board[r-1][c-1] = snum
    snum += 1

# 1 위 2 아래 3 오른쪽 4 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
reverse = [1, 0, 3, 2]

for fisher in range(C):
    # C열의 상어 잡기
    for i in range(R):
        if board[i][fisher]:
            ans += shark[board[i][fisher]][4]
            shark[board[i][fisher]] = -1
            board[i][fisher] = 0
            break

    # 상어 위치 업데이트
    for s in range(1,M+1):
        if shark[s] == -1:
            continue

        remain = shark[s][2]
        x, y, d = shark[s][0], shark[s][1], shark[s][3]
        board[x][y] = 0

        while remain:
            # 그 방향으로 이동
            nx, ny = x+dx[d], y+dy[d]
            if nx >= R:
                nx = R-2
                d = reverse[d]

            elif nx < 0:
                nx = 1
                d = reverse[d]

            if ny >= C:
                ny = C-2
                d = reverse[d]

            elif ny < 0:
                ny = 1
                d = reverse[d]

            remain -= 1
            x, y = nx, ny

        shark[s] = [x, y, shark[s][2], d, shark[s][4]]
        board[x][y] = s

print(ans)
"""

# 예전에 작성중이던 미완성 코드
"""
R, C, M = map(int, input().split())
sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = [r, c, s, d]

# d 1 위 2 아래 3 오른쪽 4 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

nextloca = {1:2, 2:1, 3:4, 4:3}

ans = 0
for loca in range(C): # 낚시왕의 위치 변화
    # 낚시왕이 가장 가까운 애를 찾음
    minvalue = R+1
    for s in sharks:
        if sharks[s][1]-1 == loca: # 낚시왕의 위치와 같고,
            if sharks[s][0] < minvalue:
                minvalue = sharks[s][0]
                minindex = s

    # 낚시왕이 찜한 애를 선택
    if minvalue < R+1:
        sharks.pop(minindex)
        ans += minindex

    # 상어들의 이동
    for s in sharks:
        if sharks[s][3] == 1:
            d = sharks[s][0]+dx[sharks[s][2]] % ((N-1)*2)

        # (N-1)*2 넘어가면.... % (N-1)*2
        if 0 <= sharks[s][0]+dx[sharks[s][2]] < R and 0 <= sharks[s][1]+dy[sharks[s][2]] < C: # 이동 가능하면
            sharks[s][0] += dx[sharks[s][2]]
            sharks[s][1] += dy[sharks[s][2]]
        else: # 벽에 부딪히면
            pass
    # 겹치는 위치 있는 상어 빼기
    ss = sorted(sharks.keys(), reverse= True)
    visited = {}
    for s in ss:
        if not visited.get((sharks[s][0], sharks[s][1])):
            visited.append((sharks[s][0], sharks[s][1]))
        else:
            sharks.pop(s) # 먹힌다.

print(ans)
"""
