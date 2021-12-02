"""
10974 모든 순열
"""

def dfs(cur, depth):
    global N
    if depth >= N:
        print(*ans, sep=" ")
        return
    for i in range(1, N+1):
        if visited[i-1] == 0:
            visited[i-1] = 1
            ans[depth] = i
            dfs(i, depth+1)
            visited[i-1] = 0

N = int(input())
visited = [0] * N
ans = [0] * N

for i in range(1, N+1):
    ans[0] = i
    visited[i-1] = 1
    dfs(i, 1)
    visited[i-1] = 0
