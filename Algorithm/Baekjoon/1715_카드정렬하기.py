"""
1715 카드 정렬하기

우선순위 큐

틀렸을 때 반례
https://www.acmicpc.net/board/view/90899
4
5
6
7
8
잘못된 답 55
정답 52
"""

import heapq

N = int(input())
h = []
for i in range(N):
    heapq.heappush(h, int(input()))

ans = 0
for i in range(N-1):
    cur = heapq.heappop(h)
    nxt = heapq.heappop(h)
    ans += cur + nxt
    heapq.heappush(h, cur+nxt)

print(ans)

# 틀렸습니다
"""
import heapq

N = int(input())
h = []
for i in range(N):
    heapq.heappush(h, int(input()))

ans = 0
cur = heapq.heappop(h)
for i in range(N-1):
    nxt = heapq.heappop(h)
    cur += nxt
    ans += cur

print(ans)
"""
