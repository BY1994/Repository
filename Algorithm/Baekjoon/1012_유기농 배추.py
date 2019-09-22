"""
1012 유기농 배추

input)
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

output)
5
1

2019.09.19 PBY
"""

################################
# 계속 틀렸던 이유는 여기!!!!!!! => 런타임 에러 해결
# https://www.acmicpc.net/board/view/37591
################################
import sys
sys.setrecursionlimit(10**6)

# dfs
def findvege(i, j, M, N, bat):
    global K
    # 상하좌우
    for nx, ny in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
        if 0 <= nx < M and 0 <= ny < N and bat[nx][ny] == 1:
            K -= 1
            bat[nx][ny] = 0
            findvege(nx, ny, M, N, bat)
            # 바로 0으로 바꿔주지 않으면 함수가 무한에 빠질 수 있음? => 아님 그 자리로 들어가서 바로 0을 만들거라서 문제 없음

# input
for testcase in range(int(input())):
    ans = 0
    M, N, K = map(int, input().split())
    bat = [[0]*N for _ in range(M)]
    for row in range(K):
        x, y = map(int, input().split())
        bat[x][y] = 1

    # main
    while K > 0:
        for i in range(M):
            for j in range(N):
                if bat[i][j] == 1:
                    ans += 1
                    K -= 1
                    bat[i][j] = 0
                    findvege(i, j, M, N, bat)

    print(ans)

# 런타임 에러
"""
# bfs
def findvege(i, j, M, N, bat):
    global K
    K -= 1
    bat[i][j] = 0
    # 상하좌우
    for nx, ny in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
        if 0 <= nx < M and 0 <= ny < N and bat[nx][ny] == 1:
            findvege(nx, ny, M, N, bat)

# input
for testcase in range(int(input())):
    ans = 0
    M, N, K = map(int, input().split())
    bat = [[0]*N for _ in range(M)]
    for row in range(K):
        x, y = map(int, input().split())
        bat[x][y] = 1

    # main
    while K > 0:
        for i in range(M):
            for j in range(N):
                if bat[i][j] == 1:
                    ans += 1
                    findvege(i, j, M, N, bat)

    print(ans)
"""   
