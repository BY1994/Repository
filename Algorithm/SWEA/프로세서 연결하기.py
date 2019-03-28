"""
삼성 SW 모의고사 프로세스 연결하기

2019.03.28 PBY 최초작성
"""

# 가지치기를 해야함
# 이미 한 번 max로 찾은 core 개수보다 너무 많이 패스하면 그 뒤는 체크할 필요 없다.

def findCore(cur_idx):
    global N, nCore
    if cur_idx == 0 or cur_idx == N-1:
        nCore += sum(arr[cur_idx])
        return
    for j in range(N):
        if arr[cur_idx][j] == 1:
            if j == 0 or j == N-1:
                nCore += 1
            else: core_loca.append([cur_idx, j])
            
def isPossible(array, direction, cur_pos):
    # array 복사
    newarr = copy.deepcopy(array)
    cnt = 0
    nextx = cur_pos[0]
    nexty = cur_pos[1]
    while True:
        # break 조건
        nextx += dx[direction]
        nexty += dy[direction] 
        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N:
            break # while문 탈출
        if newarr[nextx][nexty] == 1: # 탈출한 건 아닌데 길이 막혀있다.
            return array, False, 0
        cnt += 1
        newarr[nextx][nexty] = 1 # 그 길을 체크해줌
    return newarr, True, cnt

def backtrack(array, ncore, cur_lines, nextPerson, totalperson):
    global maxcore, minline, lencore, nCore

    # 가지치기
    if (lencore+nCore - maxcore) < (totalperson+nCore -ncore): return
    if nextPerson == lencore: # 더 확인할 코어가 없으면
        if ncore > maxcore:
            maxcore = ncore
            minline = cur_lines
        elif ncore == maxcore:
            if minline > cur_lines:
                minline = cur_lines
        return
    
    newarr = copy.deepcopy(array)
    for d in range(4):
        nextarr, pos, lines = isPossible(newarr, d, core_loca[nextPerson])
        if pos:
            backtrack(nextarr, ncore+1, lines+cur_lines, nextPerson+1, totalperson+1)
    backtrack(newarr, ncore, cur_lines, nextPerson+1, totalperson+1)
    


import copy            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [] # input 저장하는 배열 (건드리면 안 됨)
    core_loca = [] # core의 위치 저장하는 배열
    nCore = 0 # 저장한 코어의 수
    
    for i in range(N):
        arr.append(list(map(int, input().split())))
        findCore(i)
    # 인풋 돌고 나오면 벽에 붙은 코어 개수가 나오고,
    # 벽에 안 붙은 코어들 위치가 만들어진다.

    # 벽에 안 붙은 코어의 전선 연결 가능은 상하좌우와 연결하지 않는 경우
    # 그러면 그 때의 배열을 만들어서 넘긴다.
    maxcore = nCore
    minline = N*N
    lencore = len(core_loca)
    # cur_loca에 0번째 애가 상하좌우
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for d in range(4):
        nextarr, pos, lines = isPossible(arr, d, core_loca[0])
        if pos:
            backtrack(nextarr, nCore+1, lines, 1, 1)
    # 상 검사하는 함수 -> 가능여부와 간선 수를 리턴
    # 왼쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 오른쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 아래쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 그리고 아무것도 간선 연결하지 않고 코어 수 안 늘려서 재귀 들어감
    backtrack(arr, nCore, 0, 1, 1)
    # 재귀함수는 현재까지 간선 수와, 코어 수와, 복사한 배열을 인자로 받음
    
    print("#%d %d" %(tc, minline))
    
"""
# 시간초과 50개 케이스 중 8개 채점
def findCore(cur_idx):
    global N, nCore
    if cur_idx == 0 or cur_idx == N-1:
        nCore += sum(arr[cur_idx])
        return
    for j in range(N):
        if arr[cur_idx][j] == 1:
            if j == 0 or j == N-1:
                nCore += 1
            else: core_loca.append([cur_idx, j])

            
def isPossible(array, direction, cur_pos):
    # array 복사
    newarr = copy.deepcopy(array)
    cnt = 0
    nextx = cur_pos[0]
    nexty = cur_pos[1]
    while True:
        # break 조건
        nextx += dx[direction]
        nexty += dy[direction] 
        if nextx < 0 or nextx >= N or nexty < 0 or nexty >= N:
            break # while문 탈출
        if newarr[nextx][nexty] == 1: # 탈출한 건 아닌데 길이 막혀있다.
            return array, False, 0
        cnt += 1
        newarr[nextx][nexty] = 1 # 그 길을 체크해줌
    return newarr, True, cnt

def backtrack(array, ncore, cur_lines, nextPerson):
    global maxcore, minline, lencore
    
    if nextPerson == lencore: # 더 확인할 코어가 없으면
        if ncore > maxcore:
            maxcore = ncore
            minline = cur_lines
        elif ncore == maxcore:
            if minline > cur_lines:
                minline = cur_lines
        return
    
    newarr = copy.deepcopy(array)
    for d in range(4):
        nextarr, pos, lines = isPossible(newarr, d, core_loca[nextPerson])
        if pos:
            backtrack(nextarr, ncore+1, lines+cur_lines, nextPerson+1)
    backtrack(newarr, ncore, cur_lines, nextPerson+1)
    


import copy            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [] # input 저장하는 배열 (건드리면 안 됨)
    core_loca = [] # core의 위치 저장하는 배열
    nCore = 0 # 저장한 코어의 수
    
    for i in range(N):
        arr.append(list(map(int, input().split())))
        findCore(i)
    # 인풋 돌고 나오면 벽에 붙은 코어 개수가 나오고,
    # 벽에 안 붙은 코어들 위치가 만들어진다.

    # 벽에 안 붙은 코어의 전선 연결 가능은 상하좌우와 연결하지 않는 경우
    # 그러면 그 때의 배열을 만들어서 넘긴다.
    maxcore = nCore
    minline = N*N
    lencore = len(core_loca)
    # cur_loca에 0번째 애가 상하좌우
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    for d in range(4):
        nextarr, pos, lines = isPossible(arr, d, core_loca[0])
        if pos:
            backtrack(nextarr, nCore+1, lines, 1)
    # 상 검사하는 함수 -> 가능여부와 간선 수를 리턴
    # 왼쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 오른쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 아래쪽 검사하는 함수 -> 가능 여부와 간선 수를 리턴
    # 그리고 아무것도 간선 연결하지 않고 코어 수 안 늘려서 재귀 들어감
    backtrack(arr, nCore, 0, 1)
    # 재귀함수는 현재까지 간선 수와, 코어 수와, 복사한 배열을 인자로 받음
    
    print("#%d %d" %(tc, minline))
"""            
