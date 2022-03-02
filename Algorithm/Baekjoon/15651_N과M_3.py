"""
15651 N과 M 3
중복을 허용하는 조합 출력
"""
def dfs(cur, depth):
    global N, M
    if depth == M:
        print(*visited)
        return
    for i in range(1, N+1):
        visited[depth] = i
        dfs(i, depth+1)

N, M = map(int, input().split())
visited = [0] * M
for i in range(1, N+1):
    visited[0] = i
    dfs(i, 1)
