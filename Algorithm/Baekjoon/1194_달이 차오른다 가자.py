"""
1194 달이 차오른다, 가자

input)
1 7
f0.F..1

5 5
....1
#1###
.1.#0
....A
.1.#.

output)
7

-1

2019.09.20 PBY
"""

# input
N, M = map(int, input().split())
miro = [0]*N
for i in range(N):
    miro[i] = input()

# find start point
for i in range(N):
    for j in range(M):
        if miro[i][j] == '0':
            current = [i, j]

# visited
visited = [[[0]*7 for i in range(M)] for j in range(N)] # visit & abcdef

# bfs
q = [[current[0], current[1], [0]*6, 0]]
qlen = 1
visited[current[0]][current[1]][0] = 1
     
ans = -1
while qlen > 0:
    print("너 몇번")
    for ind in range(qlen):
        checkx, checky, keys, dist = q.pop(0)
        print(checkx, checky, keys, dist)
        qlen -= 1
        # break while
        if miro[checkx][checky] == '1':
            qlen = 0
            break
        # 4 ways
        for nx, ny in ((checkx-1, checky), (checkx, checky-1), (checkx+1, checky), (checkx, checky+1)):
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] != '#':
                    if visited[nx][ny][0] == 0 or (visited[nx][ny][0] == 1 and visited[nx][ny][1:] != keys):
                        if 64 < ord(miro[nx][ny]) < 71:
                            if keys[ord(miro[nx][ny])-65] == 1:
                                visited[nx][ny][0] = 1
                                if 96 < ord(miro[nx][ny]) < 103: # a-f
                                    visited[nx][ny][ord(miro[nx][ny])-96] = 1
                                    keys[ord(miro[nx][ny])-97] = 1 # 이 부분이 다른 for문 돌 때 문제를 일으킴. 수정할 것!
                                q.append([nx, ny, keys, dist+1])
                                qlen += 1

                        else:
                            visited[nx][ny][0] = 1
                            if 96 < ord(miro[nx][ny]) < 103: # a-f
                                visited[nx][ny][ord(miro[nx][ny])-96] = 1
                                keys[ord(miro[nx][ny])-97] = 1
                            q.append([nx, ny, keys, dist+1])
                            qlen += 1
else:
    ans = dist+1 # while문 종료 시점의 distance
print(ans)
        
        
# 지금 필요한 거
# 1을 만나면 break 하는 거
# 현재까지 이동한 거리 카운트 하는 거
