"""
SW expert 파핑파핑 지뢰찾기

1. 데이터의 크기가 굉장히 큰데 그거를 제대로 고려 안 해주고 완전 탐색이라고 생각해서 메모리 초과가 났다.
2. 조건을 잘 안 써주면 큐에 계속 들어가서 문제였다. if 문으로 '*'인지 '.' 인지를 꼭 잘 써줘야했다. 그리고 visited 체크도 중요했다.

"""
import sys
sys.stdin = open('1868_input.txt', 'r')

from collections import deque

def checkdirections(x, y):
    m = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if 0 <= i < N and 0 <= j < N:
                if minefield[i][j] == '*': # 주변에 *이 몇개 있는지, 
                    m += 1
    return m

T = int(input())
for tc in range(1, T+1):
    # input
    N = int(input())
    minefield = []
    nMine = 0
    for _ in range(N):
        temp = input()
        templist = []
        for j in range(N):
            templist.append(temp[j])
            if temp[j] == '.':
                nMine += 1 # 지뢰 아닌 칸 몇 개인지
        minefield.append(templist)

    visited = [[0 for _ in range(N)] for __ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and minefield[i][j] == '.' and checkdirections(i, j) == 0: # 8방향이어야 들어감 (0이어야 들어옴)
                cnt += 1 # 누르러 들어올 때마다 더해줌
                q = deque([[i, j]])
                lenq = len(q)
                while q:
                    for _ in range(lenq):
                        x, y = q.popleft()
                        m = checkdirections(x, y)
                        if visited[x][y] == 0: # 아직 방문 안해야 빼줌 => 안 그러면 큐에 계속 들어감.
                            nMine -= 1 # 하나씩 지워나감
                            minefield[x][y] = m # m도 적어줌
                            visited[x][y] = 1 # 방문 체크도 넣어줌
                            if m == 0: # 이걸 인덴트 안 시켜주면 방문한 애여도 q에 계속 주변을 찾아서 넣는가? => 여기서 무한 루프 걸린 건 맞다.
                                for i2 in range(x-1, x+2):
                                    for j2 in range(y-1, y+2):
                                        if 0<=i2<N and 0<=j2<N and minefield[i2][j2] == '.' and visited[i2][j2] == 0:
                                            q.append([i2, j2])
                    lenq = len(q)
                                        
    # 다 돌고 나면 nMine를 더해줌
    print("#%d %d" %(tc, nMine+cnt))
     
                        
# 메모리 초과
"""
from collections import deque

def popping(x, y, cnt, remain):
    global minvalue, N
    # 8방향 체크
#    m = checkdirections(x,y)
#    minefield[x][y] = m
    # 가운데가 0이면, 8 방향을 다 큐에 넣음
    q = deque([[x, y]]) # 시작점 넣어주고 # 거기서부터 주변을 도는 것이니까...
    lenq = len(q)
    checkedlist = []
    while q:
#        print(minefield)
        for i in range(lenq):
            nextx, nexty = q.popleft()
            m = checkdirections(nextx, nexty)
            remain -= 1
            minefield[nextx][nexty] = m
            checkedlist.append([nextx, nexty])
            if m == 0:
                for i in range(nextx-1, nextx+2):
                    for j in range(nexty-1, nexty+2):
                        if i == nextx and j == nexty:
                            continue
                        if 0 <= i < N and 0 <= j < N:
                            if minefield[i][j] == '.': # 주변에다가 넣어줌
                                q.append([i, j])
        lenq = len(q)
#    print(minefield)
#    print(remain, cnt)
    # 큐에서 꺼내면서 8방향 체크
    # while문이 끝나면
    check = 0
    for i in range(N):
        for j in range(N):
            if minefield[i][j] == '.':
                start = [i, j]
                check = 1
                # 다음 가능한 길 이동
                popping(start[0], start[1], cnt+1, remain)
                # 돌아와서 길 복구
                for c in checkedlist:
                    minefield[c[0]][c[1]] = '.'
    if check == 0: #다음 가능한 길 없으면
       # 다음 가능한 길이 없으면....
       if remain == 0:
#           print("여기")
#           print(cnt)
           if minvalue > cnt:
               minvalue = cnt
    
    
def checkdirections(x, y):
    m = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if 0 <= i < N and 0 <= j < N:
                if minefield[i][j] == '*': # 주변에 *이 몇개 있는지, 
                    m += 1
    return m

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    minefield = []
    nMine = 0
    for i in range(N):
        temp = input()
        templist = []
        for j in range(N):
            templist.append(temp[j])
            if temp[j] == '.':
                nMine += 1 # 지뢰 아닌 시작점 개수
        minefield.append(templist)
                            
    minvalue = nMine
    for i in range(N):
        for j in range(N):
            if minefield[i][j] == '.':
                popping(i, j, 1, nMine)
                for i in range(N):
                    for j in range(N):
                        if minefield[i][j] != '*' and minefield[i][j] != '.':
                            minefield[i][j] = '.'
                #print(minefield)

    print("#%d %d" %(tc, minvalue))

    
    # 한 점씩 잡아서 시작하고,
    # 그 점에서 터지고, 주변까지 다 큐에 넣어줌
    # 그리고 다음 재귀호출로 다음 점을 잡아서 들어감

..*..
..*..
.*..*
.*...
.*...
"""
