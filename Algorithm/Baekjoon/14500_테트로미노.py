"""
BOJ 14500 테트로미노

input)
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1

output)
19
20
7

2019.10.7 PBY
"""

# 하드코딩 하려고 했는데 시간이 너무 오래걸릴 것 같다.
"""
blocks1 = [1,1,1,1]
blocks2 = [1,1,1,1]
blocks3 = [[1,1],[1,1]]
blocks4 = [[[1,1,1,0],
           [0,0,1,0]],
           [[1,1,1,0],
           [1,0,0,0]],
           [[1,1,1,0],
            [0,1,0,0]],
           [[1,1,0,0],
            [0,1,1,0]],
           [[0,1,1,0],
            [1,1,0,0]]
           ]
        
# input
N, M = map(int, input().split())
paper = [[0] for _ in range(N)]
for _ in range(N):
    paper[_] = list(map(int, input().split()))
ans = 0

# 시작점에서부터 하나씩 재귀 들어감
for x in range(N):
    for y in range(M):
        startTet(x, y, 3, paper[x][y], [])

        
print(ans)
"""


def startTet(x, y, num, cur, visited):
    global ans, N, M

    newvisited = visited[:]
    newvisited.append([x,y])
    
    # 종료조건
    if num == 0:
        # 답체크
        if cur > ans:
            ans = cur
        # 원상복구
        return

    # 문제 발견! 계속 재귀로만 가면 ㅗ 이모양을 이어서 만들 수가 없다!!!
    # 오른쪽, 아래로만 간다고 생각했는데, 그러면 ㅗ 이 모양이 안 나옴
    if y+1 < M and [x,y+1] not in visited:
        startTet(x, y+1, num-1, cur+paper[x][y+1], newvisited)
    if x+1 < N  and [x+1,y] not in visited:
        startTet(x+1, y, num-1, cur+paper[x+1][y], newvisited)
    if y > 0 and [x,y-1] not in visited:
        startTet(x, y-1, num-1, cur+paper[x][y-1], newvisited)
    if x > 0 and [x-1, y] not in visited:
        startTet(x-1, y, num-1, cur+paper[x-1][y], newvisited)
        
# input
N, M = map(int, input().split())
paper = [[0] for _ in range(N)]
for _ in range(N):
    paper[_] = list(map(int, input().split()))
ans = 0

# 시작점에서부터 하나씩 재귀 들어감
for x in range(N):
    for y in range(M):
        startTet(x, y, 3, paper[x][y], [])

# ㅗ 모양만 따로 처리
blocks1 = [[[1,1,1],
           [0,1,0]],
           [[0,1,0],
            [1,1,1]]]
blocks2 = [[[1,0],
           [1,1],
           [1,0]],
           [[0,1],
            [1,1],
            [0,1]]]

for x in range(N-1):
    for y in range(M-2):
        cur = 0
        for i in range(2):
            for j in range(3):
                if blocks1[0][i][j]: # 1&2는 0이 나온다. paper[x+i][y+j]&blocks1[0][i][j] 이면 잘못된 결과가 나온다!!!
                    cur += paper[x+i][y+j]
        if cur > ans:
            ans = cur
        cur = 0
        for i in range(2):
            for j in range(3):
                #print(paper[x+i][y+j], blocks1[1][i][j], end=" ")
                if blocks1[1][i][j]:
                    cur += paper[x+i][y+j]
        #print()
        #print(cur, ans)
        if cur > ans:
            ans = cur

for x in range(N-2):
    for y in range(M-1):
        cur = 0
        for i in range(3):
            for j in range(2):
                if blocks2[0][i][j]:
                    cur += paper[x+i][y+j]
        if cur > ans:
            ans = cur
        cur = 0
        for i in range(3):
            for j in range(2):
                if blocks2[1][i][j]:
                    cur += paper[x+i][y+j]
        if cur > ans:
            ans = cur
        
print(ans)

