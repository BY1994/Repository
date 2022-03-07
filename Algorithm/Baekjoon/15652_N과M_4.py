"""
15652 N과 M 4
"""
def dfs(cur, depth):
    global N, M
    if depth == M:
        print(*visited)
        return
    for i in range(cur, N):
        visited[depth] = i+1
        dfs(i, depth+1)

N, M = map(int, input().split())
visited = [0] * M
for i in range(N):
    visited[0] = i+1
    dfs(i, 1)
