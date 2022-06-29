"""
15903 카드 합체 놀이

우선순위 큐
"""

import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
h = []

for i in range(n):
    heapq.heappush(h, (cards[i], i))

for i in range(m):
    card1, id1 = heapq.heappop(h)
    card2, id2 = heapq.heappop(h)
    new = card1 + card2
    cards[id1] = new
    cards[id2] = new
    heapq.heappush(h, (new, id1))
    heapq.heappush(h, (new, id2))

print(sum(cards))
