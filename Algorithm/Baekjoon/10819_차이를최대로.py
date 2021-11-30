"""
10819 차이를 최대로
"""

def dfs(cur, depth, s):
    global ans, N
    if depth >= N:
        ans = max(ans, s)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, depth+1, s + abs(A[cur]-A[i]))
            visited[i] = 0

ans = 0
N = int(input())
visited = [0] * N
A = list(map(int, input().split()))

for i in range(N):
    visited[i] = 1
    dfs(i, 1, 0)
    visited[i] = 0

print(ans)
