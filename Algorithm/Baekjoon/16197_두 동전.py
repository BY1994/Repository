"""
16197 두 동전

2019.04.16 PBY 최초 작성

딕셔너리에는 튜플만 들어갈 수 있다.
visited에 추가해주는 줄 하나를 추가 안 해서 엄청 오래 돌았다. => 시간 초과 해결!

"""

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        board[i].append(temp[j])

coins = []
# 두 동전 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append([i, j])
            board[i][j] = '.' # 공 빼내기

visited = {}
q = [coins[0]+coins[1]]
lenq = 1
visited[(coins[0][0], coins[0][1]), (coins[1][0], coins[1][1])] = 1

cnt = 1 # 몇 번 돌았는지
possible = 0
# 4 방향으로 bfs 넣기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    if cnt == 11: # 10 번 돌았으면 끝 => 이걸 10이라고 해서 틀렸다....
        break
    for l in range(lenq):
        x1, y1, x2, y2 = q.pop(0)
        # 4방향으로 돌기
        for d in range(4):
            coinnum = 2  # coin이 2개 있음
            # 이동하려는 칸이 벽이면 이동하지 않는다
            if 0 <= x1+dx[d] < N and 0 <= y1 + dy[d] < M:
                if board[x1+dx[d]][y1+dy[d]] == '.': # 벽이 아니면
                    newx1 = x1+dx[d]; newy1 = y1+dy[d] # x1 += dx[d]; y1 += dy[d]
                else:
                    newx1 = x1; newy1 = y1
            else:
                # 칸을 벗어났으면
                coinnum -= 1

            # visited가 아니면 큐에 넣는다.
            # 이동하려는 칸이 있으면 이동한다
            # visited가 아니면 큐에 넣는다
            # 이동하려는 칸이 N, M을 벗어나면 coin 개수 하나 빼고

            if coinnum == 1:
                possible = 1
                break
            elif coinnum == 2: # 동전 안 빠지면 그냥 이동
                if not visited.get((newx1, newy1, newx2, newy2)):
                    q.append([newx1, newy1, newx2, newy2])
                    visited[(newx1, newy1, newx2, newy2)] = 1

        if possible == 1:
            break
    if possible == 1:
        break

    lenq = len(q)
    cnt += 1

if possible == 0:
    print(-1)
else:
    print(cnt)

"""
N, M = map(int,input().split())
mat = []
coins = []
padding = ['1' * (M + 2)]
for _ in range(N):
    temp = '1' + input() + '1'
    for __ in range(len(temp)):
        if temp[__] == 'o':
            coins.append([_, __])
    mat.append(temp)
mat = padding + mat + padding

"""







































