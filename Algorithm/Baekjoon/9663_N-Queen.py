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
"""

N = int(input())
cnt = 0 # 경우의 수
used = [0]*N
for i in range(N): # 시작점
    nqueens(i, 0) # 매 시작점을 시작으로 들어가도록
# DFS 높이 들어갈 때, x좌표는 depth+1로 고정

def nqueens(y, depth):
    global cnt
    if depth == N: # 함수 바깥의 변수를 읽는 건 가능
        cnt += 1
    else:
        # 재귀함수 구현
        # 대각선 위치 체크하는 함수 따로 두기
        nextys = checkdiagonal(depth) # 그 때의 used를 가지고 체크
        # 다음 가능한 위치, 지금까지 온 used 변수 이용 - 순열
        used[depth] = 1
        for nexty in nextys:
            nqueens(nexty)
        used[depth] = 0
        
def checkdiagonal(depth): 
    # 그 때의 used를 가지고 체크
    nextys_temp = [1] * N # 갈 수 있다고 체크
    for i in range(depth):
        if used[i] == 1: # used가 체크되었으면
            # 왼쪽 대각선 확인
            
            # 오른쪽 대각선 확인
    return 


# visual studio는 실행시 ctrl + f5

