# 234 D

import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

h = []
for i in range(K):
    heapq.heappush(h, P[i])

cur = heapq.heappop(h)
print(cur)
heapq.heappush(h, cur)

for i in range(K, N):
    if P[i] < cur:
        print(cur)
        continue
    heapq.heappush(h, P[i])
    heapq.heappop(h)
    cur = heapq.heappop(h)
    print(cur)
    heapq.heappush(h, cur)
