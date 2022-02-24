"""
15650 N 과 M 2
"""

def dfs(depth, cur):
    global N, M
    if depth == M-1:
        print(*visited)
        return

    for i in range(cur+1, N+1):
        visited[depth+1] = i
        dfs(depth+1, i)

N, M = map(int, input().split())

visited = [0] * M

for i in range(1, N+1):
    visited[0] = i
    dfs(0, i)
