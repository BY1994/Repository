"""
12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
"""

# 거꾸로 올라가기
# 이미 간 지점은 다시 안 가도록??
def movePipe(xy, d):
    global cnt, N
    if xy[0] == N-1 and xy[1] == N-1:
        cnt += 1
        return

    if d == 1: # 가로
        if xy[1] + 1 < N and home[xy[0]][xy[1]+1] == '0': #가로로 갈 수 있다.
            movePipe([xy[0], xy[1]+1], 1)
        if xy[1] + 1 < N and xy[0] + 1 < N: # 대각선으로 갈 수 있다.
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1], 3)
    elif d == 2: # 세로
        if xy[0] + 1 < N and home[xy[0]+1][xy[1]] == '0':
            movePipe([xy[0]+1, xy[1]], 2)
        if xy[1] + 1 < N and xy[0] + 1 < N:
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1],3)
    elif d == 3: # 대각선
        if xy[1] + 1 < N and home[xy[0]][xy[1]+1] == '0': #가로로 갈 수 있다.
            movePipe([xy[0], xy[1]+1], 1)
        if xy[0] + 1 < N and home[xy[0]+1][xy[1]] == '0':
            movePipe([xy[0]+1, xy[1]], 2)
        if xy[1] + 1 < N and xy[0] + 1 < N:
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1],3)

N = int(input())
home = []
for _ in range(N):
    home.append(input().split())

start = (0,1) # 가로
cnt = 0

movePipe(start, 1)
print(cnt)

"""
import time
start_time = time.time()

def movePipe(xy, d):
    global cnt, N
    if xy[0] == N-1 and xy[1] == N-1:
        cnt += 1
        return

    if d == 1: # 가로
        if xy[1] + 1 < N and home[xy[0]][xy[1]+1] == '0': #가로로 갈 수 있다.
            movePipe([xy[0], xy[1]+1], 1)
        if xy[1] + 1 < N and xy[0] + 1 < N: # 대각선으로 갈 수 있다.
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1], 3)
    elif d == 2: # 세로
        if xy[0] + 1 < N and home[xy[0]+1][xy[1]] == '0':
            movePipe([xy[0]+1, xy[1]], 2)
        if xy[1] + 1 < N and xy[0] + 1 < N:
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1],3)
    elif d == 3: # 대각선
        if xy[1] + 1 < N and home[xy[0]][xy[1]+1] == '0': #가로로 갈 수 있다.
            movePipe([xy[0], xy[1]+1], 1)
        if xy[0] + 1 < N and home[xy[0]+1][xy[1]] == '0':
            movePipe([xy[0]+1, xy[1]], 2)
        if xy[1] + 1 < N and xy[0] + 1 < N:
            if home[xy[0]][xy[1]+1] == '0' and home[xy[0]+1][xy[1]] == '0' and home[xy[0]+1][xy[1]+1]=='0':
                movePipe([xy[0]+1, xy[1]+1],3)

N = int(input())
home = []
for _ in range(N):
    home.append(input().split())

start = (0,1) # 가로
cnt = 0

movePipe(start, 1)
print(cnt)
print(start_time)
print("---%s seconds---" %(time.time() - start_time))
"""
