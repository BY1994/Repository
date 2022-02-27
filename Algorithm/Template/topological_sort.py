# topological sort
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N
ans = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

q = []
for node in range(N):
    if indegree[node] == 0:
        q.append([node, 1])

while q:
    cur, dist = q.pop(0)
    ans[cur] = dist

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append([node, dist+1])

for node in range(N):
    print(ans[node], end=" ")
print()


# topological sort with priority queue
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
