"""
1417 국회의원 선거

입력의 크기가 작기 때문에 하나씩 확인해도 가능함

python 의 heapq 는 min heap 이다. (max heap 으로 쓰려면 -1 곱해야함)
"""

import heapq
h = []
N = int(input())
DASOM = int(input())
for i in range(1, N):
    can = int(input())
    if can >= DASOM:
        heapq.heappush(h, -1*can)

ans = 0
while h:
    cur = -1*heapq.heappop(h)
    if DASOM > cur:
        continue
    DASOM += 1
    cur -= 1
    ans += 1
    if cur >= DASOM:
        heapq.heappush(h, -1*cur)
print(ans)
