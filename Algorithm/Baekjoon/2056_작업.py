"""
2056 작업

"""

N = int(input())
time = [0] * N
graph = [[] for _ in range(N)]
indegree = [0] *N
max_parent = [0] * N
ans = [0] * N
for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    for j in range(_input[1]):
        graph[i].append(_input[2+j]-1)
        indegree[_input[2+j]-1] += 1
        
q = []

for i in range(N):
    if indegree[i] == 0:
        q.append([i, time[i]])

while q:
    cur, t = q.pop(0)
    ans[cur] = t

    for node in graph[cur]:
        indegree[node] -= 1
        if max_parent[node] < t:
            max_parent[node] = t
        if indegree[node] == 0:
            q.append([node, max_parent[node]+time[node]])

print(max(ans))
