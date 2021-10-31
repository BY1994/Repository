"""
2252 줄 세우기

https://www.acmicpc.net/board/view/74119
반례
5 4
2 3
1 2
4 2
5 2

답
1 4 5 2 3
"""
"""
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

q = deque()
for node in range(N):
    if indegree[node] == 0:
        q.append(node)
 
while q:
    cur = q.popleft()
    print(cur+1, end=" ")
 
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
print()
"""
# 시간 초과 deque로 바꿔야지
# deque 문제가 아니라 grpah = [[]] * N 해서 얕은 복사로 만든게 문제였다

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

q = []
for node in range(N):
    if indegree[node] == 0:
        q.append(node)
 
while q:
    cur = q.pop(0)
    print(cur+1, end=" ")
 
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
print()
