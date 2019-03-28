""" 
9663 N-Queen
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

최초작성 2019.03.13 PBY
수정 2019.03.23 PBY => 시간초과
"""

# 순열
def nqueen(k, n):
    global ans
    if k == n: # 종료조건
        ans += 1
        #print("찾았다")
        return

    #if ans > 0:
    #    return
    
    for i in range(n): # 세로마다
        if used[i] == False: # 세로, 열
            # 대각선체크
            for j in range(k):
                if j-perm[j] == k-i: # 오른쪽 아래 대각선
                    break
                if -(j-k) == perm[j]-i: #왼쪽 아래 대각선
                    break
            else:
                used[i] = True
                perm[k] = i
                nqueen(k+1, n)
                used[i] = False

# 대각선 배열 저장 =>perm
N = int(input())
used = [False]*N
perm = [0]*N
ans = 0
for i in range(N):
    used[i] = True
    perm[0] = i
    nqueen(1, N)
    used[i] = False


print(ans)
"""
# 시간초과
import copy


def NQueen(array, xy):
    global ans, N
    if xy[0] == N-1:
        ans += 1
        return

    newchess = copy.deepcopy(array)
    candidates = checkPossible(newchess, xy)
    for c in candidates:
        NQueen(newchess, c)

def checkPossible(array, xy):
    global N
    # 세로줄 다 체크하기
    for j in range(N):
        array[j][xy[1]] = 1

    # 대각선 왼쪽 아래 체크하기
    j = xy[1]
    for i in range(xy[0]+1, N):
        if j > 0:
            array[i][j-1] = 1
            j -= 1
            
    # 대각선 오른쪽 아래 체크하기
    j = xy[1]
    for i in range(xy[0]+1, N):
        if j < N-1:
            array[i][j+1] = 1
            j += 1

    # 체크하고 남은 가능한 candidates 찾기
    candidates = []
    for j in range(N):
        if array[xy[0]+1][j] == 0:
            candidates.append([xy[0]+1, j])

    return candidates


N = int(input())
chess = [[0 for _ in range(N)] for __ in range(N)]
ans = 0

# 처음 갈 수 있는 위치들 체크해서 넘기기
for i in range(N):
    newchess = copy.deepcopy(chess)
    candidates = checkPossible(newchess, (0, i))
    for c in candidates:
        NQueen(newchess, c)

print(ans)
"""

"""
작성하다 만 코드
N = int(input())
cnt = 0 # 경우의 수
used = [0]*N
for i in range(N): # 시작점
    used[0] = i
    nqueens(0, i) # 매 시작점을 시작으로 들어가도록
# DFS 높이 들어갈 때, x좌표는 depth+1로 고정

def nqueens(x, y):
    global cnt
    if x == N: # 함수 바깥의 변수를 읽는 건 가능
        cnt += 1
    else:
        # 재귀함수 구현
        # 대각선 위치 체크하는 함수 따로 두기
        nextys = checkdiagonal(x) # 그 때의 used를 가지고 체크
        # 다음 가능한 위치, 지금까지 온 used 변수 이용 - 순열
        for nexty in nextys:
            used[x] = nexty
            nqueens(x+1, nexty)
        
def checkdiagonal(depth): 
    # 그 때의 used를 가지고 체크
    nextys_temp = [1] * N # 갈 수 있다고 체크
    for i in range(depth):
        if used[i] == depth:
        if used[i] == 1: # used가 체크되었으면
            # 왼쪽 대각선 확인
            
            # 오른쪽 대각선 확인
    return nextys_temp
"""

"""
N = int(input())
if N == 1:
    print("1")
elif N == 2:
    print("0")
elif N == 3:
    print("0")
elif N == 4:
    print("2")
elif N == 5:
    print("10")
elif N == 6:
    print("4")
elif N == 7:
    print("40")
elif N == 8:
    print("92")
elif N == 9:
    print("352")
elif N == 10:
    print("724")
elif N == 11:
    print("2680")
elif N == 12:
    print("14200")
elif N == 13:
    print("73712")
elif N == 14:
    print("365596")
"""

"""
ans = [0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184]
print(ans[int(input())])
"""
# visual studio는 실행시 ctrl + f5

