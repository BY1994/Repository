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
    
