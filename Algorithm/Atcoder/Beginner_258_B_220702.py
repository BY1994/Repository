"""
Atcoder 258 (2022.07.02)

모든 경우의 수에 대해 한 방향으로만 탐색해서 최대 숫자 찾기
한 방향으로 전진이라 visited 배열 필요 없었음
"""

def dfs(x, y, d, cur):
    global N

    temp[cur-1] = A[x][y]
    if cur >= N:        
        return
    nx, ny = (x+N+ nextd[d][0])%N, (y + N+ nextd[d][1])%N
    dfs(nx,ny,d,cur+1)

nextd = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
N = int(input())
A = []
for i in range(N):
    A.append(input())

temp = [0]*N
ans = 0

for i in range(N):
    for j in range(N):
        for d in range(8):
            dfs(i, j, d, 1)
            res = int(''.join(temp))
            if res > ans:
                ans = res

print(ans)
