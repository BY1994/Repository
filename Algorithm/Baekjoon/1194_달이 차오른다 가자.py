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

7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1


output)
7

-1

55

2019.09.20 PBY
최종 제출 2021.09.23
"""
# test용
# 1 7
# F.0..f1

# 런타임에러
# 50 * 50 * 2^6 = 160,000

# 그래도 런타임에러
# visited 배열을 가장 마지막으로 지나간 key 로 덮어썼기 때문

# 1 << 7 해놓고 함수는 여전히 index + 1 이랑 시작 key 를 1 로 해둬서 틀렸습니다 나옴

# 런타임에러 해결
# queue 종료 조건을 qe >= qs 라고 하는 바람에 queue 폭발 => 런타임에러 (IndexError) 발생

# 시간 단축 bfs 를 함수로 바꿔서 바로 return 하도록 변경 444ms -> 368 ms
# 시간 단축 ord 를 숫자로 변경 -> 348 ms
# 시간 단축 and 말고 <= <= 로 변경하니까 308 ms
# 시간 단축 x + dx[d] 를 nx로, y + dy[d] 를 ny 로 변경하니까 272 ms
# 시간 단축 ord(miro[nx][ny]) 를 np 변수로, ord('A') 남은 거를 숫자로 바꿨는데 296 ms...
# 시간 단축 불필요한 if 문 줄이고 다 and 로 조건 연결 276 ms
# 시간 단축 find_start로 0 찾자마자 return 종료하도록 변경 360 ms 
# 시간 단축 queue 사이즈를 200,000 에서 queue.append 로 바꾸니까 164 ms
# 시간 단축 배열을 만드는 것 자체에 상당한 시간이 소요되는 것 같아서 1<<6으로 변경 148 ms
# 시간 단축 input 배열 받을 때 [0] 된 거를 문자열로 바꾸는데 시간이 소요될까 싶어서 input() 을 list 로 받도록 수정 160 ms
# 시간 단축 list인 q.pop(0) 을 deque로 바꿔서 q.popleft()로 변경 188 ms
# 시간 단축 stdin.readline으로 input 읽기 200 ms

from collections import deque
import sys
input = sys.stdin.readline

def set_key(key, index):
    return key | (1 << index)

def check_door(key, index):
    return (1 << index) & key

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
miro = [input() for _ in range(N)]

# find start point
def find_start():
    for i in range(N):
        for j in range(M):
            if miro[i][j] == '0':
                return i, j

sx, sy = find_start()

visited = [[[0]*(1<<6) for _ in range(M)] for __ in range(N)]
que = deque() # x,y,dist,keys

que.append([sx, sy, 0, 0])
visited[sx][sy][0] = 1

def bfs():
    while que:
        x, y, dist, key = que.popleft()

        for d in range(4):
            nkey = key
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] != '#' and not visited[nx][ny][key]:
                np = ord(miro[nx][ny])
                if miro[nx][ny] == '1':
                    return dist+1
                elif 65 <= np <= 70 and not check_door(key, np - 65): # ord('F'), ord('A')
                        continue
                elif 97 <= np <= 102: # ord('f') ord('a')
                        nkey = set_key(key, np - 97)
                que.append([nx, ny, dist + 1, nkey])
                visited[nx][ny][nkey] = 1
    else:
        return -1

print(bfs())

# 최초 통과 코드 444 ms
"""
def set_key(key, index):
    return key | (1 << index)

def check_door(key, index):
    return (1 << index) & key

keys = 0 # 열쇠 아무것도 없이는 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
miro = [0]*N
for i in range(N):
    miro[i] = input()

# find start point
for i in range(N):
    for j in range(M):
        if miro[i][j] == '0':
            current = [i, j]
#        elif miro[i][j] == '1': # 도착점이 한 곳이 아님
#            final = [i, j]

visited = [[[0]*(1<<7) for _ in range(M)] for __ in range(N)]
que = [[0] * 4 for _ in range(200000)] # x,y,dist,keys
qs = 0
qe = 1

que[qs][0] = current[0]
que[qs][1] = current[1]
que[qs][2] = 0 # dist
que[qs][3] = keys
visited[current[0]][current[1]][keys] = 1

flag = 0
while qe > qs:
    qs += 1
    x = que[qs-1][0]
    y = que[qs-1][1]
    dist = que[qs-1][2]
    key = que[qs-1][3]
    #print("### qs")
    #print(x, y, dist, key)

    for d in range(4):
        nkey = key
        if x + dx[d] < N and x + dx[d] >= 0 and y + dy[d] < M and y + dy[d] >= 0:
            if miro[x + dx[d]][y + dy[d]] == '#': continue
            if visited[x + dx[d]][y + dy[d]][key]: continue
            if miro[x + dx[d]][y + dy[d]] == '1':
                print(dist+1)
                flag = 1
                break
            if ord(miro[x + dx[d]][y + dy[d]]) <= ord('F') and \
               ord(miro[x + dx[d]][y + dy[d]]) >= ord('A'):
                if not check_door(key, ord(miro[x + dx[d]][y + dy[d]]) - ord('A')):
                    continue
            if ord(miro[x + dx[d]][y + dy[d]]) <= ord('f') and \
               ord(miro[x + dx[d]][y + dy[d]]) >= ord('a'):
                    nkey = set_key(key, ord(miro[x + dx[d]][y + dy[d]]) - ord('a'))
                    
            que[qe][0] = x + dx[d]
            que[qe][1] = y + dy[d]
            que[qe][2] = dist + 1
            que[qe][3] = nkey
            qe += 1
            visited[x + dx[d]][y + dy[d]][nkey] = 1
            #print("### qe")
            #print(x + dx[d], y + dy[d], dist+1, key)
                    
    if flag == 1:
        break
else:
    print(-1)
"""

# 테스트 못해봤지만 아래 코드도 시간초과일 것으로 예상됨
"""
# 그냥 시간초과일 수 있음 -> 덱이랑 input보다 빠른 거
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
# 덮어씌우면 가야되는 길을 안 가는 문제?
# https://www.acmicpc.net/board/view/14952
visited = [[[0]*7 for i in range(M)] for j in range(N)] # visit & abcdef

# bfs
q = [[current[0], current[1], [0]*6, 0]]
qlen = 1
visited[current[0]][current[1]][0] = 1
     
ans = -1
while qlen > 0:
    # queue에서 하나씩 꺼내기
    for ind in range(qlen):
        checkx, checky, keys, dist = q.pop(0)
        qlen -= 1
        
        # while 문 break 조건 (목적지 도달)
        if miro[checkx][checky] == '1':
            flag = 1
            qlen = 0
            break
        
        # 4 ways 방향으로 다음 진로 선택
        for nx, ny in ((checkx-1, checky), (checkx, checky-1), (checkx+1, checky), (checkx, checky+1)):
            flag = 0
            # 길이 막히지 않고
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] != '#':
                    # 방문하지 않은 곳
                    # visited 퇴화...? 덮어씌움 문제....
                    if visited[nx][ny][0] == 0 or (visited[nx][ny][0] == 1 and visited[nx][ny][1:] != keys): # 시간초과 의심 구간
                        if 64 < ord(miro[nx][ny]) < 71: # 대문자
                            if keys[ord(miro[nx][ny])-65] == 1:
                                visited[nx][ny][0] = 1
                                visited[nx][ny][1:] = keys
                                q.append([nx, ny, keys, dist+1])
                                qlen += 1
                                flag = 1

                        else:
                            visited[nx][ny][0] = 1
                            keys2 = keys[:] # 문제 해결 리스트가 계속 변형되어서 열쇠 찾은 후 인지 못함
                            if 96 < ord(miro[nx][ny]) < 103: # a-f
                                keys2[ord(miro[nx][ny])-97] = 1
                            visited[nx][ny][1:] = keys2
                            q.append([nx, ny, keys2, dist+1])
                            qlen += 1
                            flag = 1
        if qlen == 0 and flag == 0:
            break
    if qlen == 0 and flag == 0:
        break
else:
    ans = dist # while문 종료 시점의 distance
print(ans)
"""

# 시간초과
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
    # queue에서 하나씩 꺼내기
    for ind in range(qlen):
        checkx, checky, keys, dist = q.pop(0)
        qlen -= 1
        
        # while 문 break 조건 (목적지 도달)
        if miro[checkx][checky] == '1':
            flag = 1
            qlen = 0
            break

        # 4 ways 방향으로 다음 진로 선택
        for nx, ny in ((checkx-1, checky), (checkx, checky-1), (checkx+1, checky), (checkx, checky+1)):
            flag = 0
            # 길이 막히지 않고
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] != '#':
                    # 방문하지 않은 곳
                    if visited[nx][ny][0] == 0 or (visited[nx][ny][0] == 1 and visited[nx][ny][1:] != keys):
                        if 64 < ord(miro[nx][ny]) < 71: # 대문자
                            if keys[ord(miro[nx][ny])-65] == 1:
                                visited[nx][ny][0] = 1
                                visited[nx][ny][1:] = keys
                                q.append([nx, ny, keys, dist+1])
                                qlen += 1
                                flag = 1

                        else:
                            visited[nx][ny][0] = 1
                            keys2 = keys[:] # 문제 해결 리스트가 계속 변형되어서 열쇠 찾은 후 인지 못함
                            if 96 < ord(miro[nx][ny]) < 103: # a-f
                                keys2[ord(miro[nx][ny])-97] = 1
                            visited[nx][ny][1:] = keys2
                            q.append([nx, ny, keys2, dist+1])
                            qlen += 1
                            flag = 1
        if qlen == 0 and flag == 0:
            break
    if qlen == 0 and flag == 0:
        break
else:
    ans = dist # while문 종료 시점의 distance
print(ans)
        
        
# 지금 필요한 거
# 1을 만나면 break 하는 거
# 현재까지 이동한 거리 카운트 하는 거
"""
