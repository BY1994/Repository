"""
1753 최단 경로

다익스트라

제출 전에 반례가 없을까 해서 돌려봤는데, 문제 없음
https://www.acmicpc.net/board/view/81206
4 1 
1
4 2 3
0
INF
INF
INF
"""

# min heap 인데, max heap 인 줄 알고 - 붙였음
import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
dist = [300100 for i in range(V+1)]
cost = [[] for i in range(20001)]
cost_ind = [0 for i in range(20001)]

for _ in range(E):
    u, v, w = map(int, input().split())

    cost[u].append((v,w))
    cost_ind[u] += 1

h = []
heapq.heappush(h, (0, K))
dist[K] = 0

while h:
    c, cur_node = heapq.heappop(h)

    for i in range(cost_ind[cur_node]):
        next_cost = c + cost[cur_node][i][1]
        if dist[cost[cur_node][i][0]] <= next_cost: continue
        dist[cost[cur_node][i][0]] = next_cost
        heapq.heappush(h, (next_cost, cost[cur_node][i][0]))

for i in range(1,V+1):
    if dist[i] == 300100:
        print("INF")
    else:
        print(dist[i])

# 메모리 문제 생길 것 (실행 안 됨...)
"""
import heapq

V, E = map(int, input().split())
K = int(input())
dist = [300100 for i in range(V+1)]
cost = [[0 for i in range(20001)] for j in range(20001)]
connect = [[0 for i in range(20001)] for j in range(20001)]

for _ in range(E):
    u, v, w = map(int, input().split())

    cost[u][v] = w
    cost[v][u] = w
    connect[u][0] += 1
    connect[u][connect[u][0]] = v
    connect[v][0] += 1
    connect[v][connect[v][0]] = u

h = []
heapq.push(h, (0, K))
dist[K] = 0

while h:
    c, cur_node = heapq.pop(h)

    for i in range(connect[cur_node][0]):
        next_cost = -c + cost[cur_node][i+1]
        if dist[connect[cur_node]][i+1] <= next_cost: continue
        dist[connect[cur_node]][i+1] = next_cost
        heapq.push(h, (-next_cost, i+1))

for i in range(1,V+1):
    if dist[i] == 300100:
        print("INF")
    else:
        print(dist[i])
"""
