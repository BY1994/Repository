"""
11724 연결 요소의 개수

BFS 로 풀어도 되는 문제이지만 코드가 깔끔하게 안 짜져서 DFS로 도전
4963 섬의 개수처럼 섬의 개수를 세는 문제
하지만 문제 형식이 달라서 아직 같은 문제처럼 안 보인다.

2022.06.16 PBY 최초 작성
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global N

    for i in range(1,N+1):
        if graph[x][i] == 1:
            graph[x][i] = 0
            graph[i][x] = 0
            visited[i] = 0
            dfs(i)

N, M = map(int, input().split())
graph = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    visited[u] = 1
    visited[v] = 1

ans = 0
for i in range(N):
    if visited[i] == 1:
        ans += 1
        visited[i] = 0
        dfs(i)

print(ans)
