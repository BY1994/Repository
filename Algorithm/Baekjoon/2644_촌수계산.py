"""
2644 촌수계산

BFS
"""

n = int(input())
a, b = map(int, input().split())
m = int(input())
edge = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)
visited = [0] * (n+1)

q = [(a,0)]
visited[a] = 1
qs = 0
qe = 1
while qs < qe:
    cur, dist = q[qs]
    qs += 1

    if cur == b:
        print(dist)
        break

    for nxt in edge[cur]:
        if visited[nxt] == 1:
            continue
        q.append((nxt, dist+1))
        qe += 1
        visited[nxt] = 1
else:
    print(-1)
