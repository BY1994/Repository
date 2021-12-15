"""
1966 프린터 큐
시뮬레이션
"""

import heapq

for _ in range(int(input())):
    docind = 0
    ans = 0
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    check = [0] * N
    check[M] = 1

    h = []
    for i in range(N):
        heapq.heappush(h, -1*doc[i])

    while(h):
        _max = -1 * heapq.heappop(h)
        if doc[docind] == _max:
            if check[docind] == 1:
                print(ans+1)
                break
            ans += 1
        else:
            heapq.heappush(h, -1 * _max)
            doc.append(doc[docind])
            check.append(check[docind])
        docind += 1
