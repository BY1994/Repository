"""
1766 문제집
"""
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    indegree[B-1] += 1

heap = []

for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    cur = heapq.heappop(heap)

    print(cur+1, end = " ")

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            heapq.heappush(heap, node)
