"""
14567 선수과목

위상 정렬
"""

# 시간초과
# 선수과목 A, B가 항상 새로운 게 들어오는 게 아닌가?!
# pypy3 로 제출하고 AC

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
