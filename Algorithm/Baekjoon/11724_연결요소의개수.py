"""
11724 연결 요소의 개수

BFS 로 풀어도 되는 문제이지만 코드가 깔끔하게 안 짜져서 DFS로 도전
4963 섬의 개수처럼 섬의 개수를 세는 문제
하지만 문제 형식이 달라서 아직 같은 문제처럼 안 보인다.

2022.06.16 PBY 최초 작성
2022.06.17 PBY 통과
"""

# 틀렸던 이유는 간선이 없는 노드는 없는 거라고 생각했기 때문
# https://www.acmicpc.net/board/view/68534

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x):
    global N

    for i in range(1, graph[x][0]+1):
        nx = graph[x][i]
        if visited[nx] == 1:
            visited[nx] = 0
            dfs(nx)

N, M = map(int, input().split())
graph = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [1] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u][0] += 1
    graph[u][graph[u][0]] = v
    graph[v][0] += 1
    graph[v][graph[v][0]] = u

ans = 0
for i in range(1, N+1):
    if visited[i] == 1:
        ans += 1
        visited[i] = 0
        dfs(i)

print(ans)

# 시간초과 및 틀렸습니다
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
"""
