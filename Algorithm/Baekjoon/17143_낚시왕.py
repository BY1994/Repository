"""
17143 낚시왕

2019.04.17 PBY 최초작성
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
        if sharks[s][3] == 1
            d = sharks[s][0]+dx[sharks[s][2]] % ((N-1)*2)

        # (N-1)*2 넘어가면.... % (N-1)*2
        if 0 <= sharks[s][0]+dx[sharks[s][2]] < R and 0 <= sharks[s][1]+dy[sharks[s][2]] < C: # 이동 가능하면
            sharks[s][0] += dx[sharks[s][2]]
            sharks[s][1] += dy[sharks[s][2]]
        else: # 벽에 부딪히면

    # 겹치는 위치 있는 상어 빼기
    ss = sorted(sharks.keys(), reverse= True)
    visited = {}
    for s in ss:
        if not visited.get((sharks[s][0], sharks[s][1])):
            visited.append((sharks[s][0], sharks[s][1]))
        else:
            sharks.pop(s) # 먹힌다.

print(ans)