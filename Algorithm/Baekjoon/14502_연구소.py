"""
14502 연구소
"""

def dfs(x, y, depth):
    if depth == 3:
        q = []
        
        # bfs
        # visited 이용
    # i, j 다음 거 dfs()

mymap = []
vind = 3
visited = [[0 for i in range(M)] for j in range(N)]
N, M = map(int, input().split())
for _ in range(N):
    mymap.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if mymap[i][j] == 0:
            mymap[i][j] = 1
            dfs(i, j, 1)
            mymap[i][j] = 0
