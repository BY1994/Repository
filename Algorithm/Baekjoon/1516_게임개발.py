"""
1516 게임 개발

반례
https://www.acmicpc.net/board/view/15062
https://www.acmicpc.net/board/view/17781
"""

# 기본 위상 정렬과 선후 관계가 반대로 들어오는구나!!
# 그리고 부모의 max 값을 가지고 있어야한다

N = int(input())
graph = [[] for _ in range(N)]
indegree = [0] * N
max_parent = [0] * N
time = [0] * N
ans = [0] * N
for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    j = 1
    while (_input[j] != -1):
        graph[_input[j] - 1].append(i)
        indegree[i] += 1
        j += 1
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

for i in range(N):
    print(ans[i])

# Wrong Answer
"""
N = int(input())
graph = [[] for _ in range(N)]
indegree = [0] * N
min_time = [0] * N
time = [0] * N
for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    j = 1
    while (_input[j] != -1):
        graph[_input[j] - 1].append(i)
        indegree[i] += 1
        j += 1
q = []

for i in range(N):
    if indegree[i] == 0:
        q.append([i, time[i]])

while q:
    cur, t = q.pop(0)
    min_time[cur] = t

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append([node, t+time[node]])

for i in range(N):
    print(min_time[i])
"""
