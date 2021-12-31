"""
1806 부분합

풀이 참고
https://velog.io/@nacean/%EB%B0%B1%EC%A4%801806-%EB%B6%80%EB%B6%84%ED%95%A9-C-%ED%92%80%EC%9D%B4

반례 모음
https://bingorithm.tistory.com/13
"""

import sys

N, S = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

p1 = 0
p2 = 0
ans = 100001
cur = numbers[p1]
length = 1

while p1 <= p2:
    if cur >= S:
        if ans > length:
            ans = length
        cur -= numbers[p1]
        p1 += 1
        length -= 1
    else:
        p2 += 1
        length += 1
        if p2 >= N:
            break
        cur += numbers[p2]

if ans == 100001:
    print(0)
else:
    print(ans)

# 너무 복잡하게 풀이하려고 한 듯
# 단순히 p2 늘리다가 S 넘으면 p1 을 줄여야함
"""
import sys

N, S = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

p1 = 0
p2 = 0
ans = 100000
length = 1
cur = numbers[p1]

if cur >= S:
    ans = length

while p1 < N:
    print("p1 p2 cur",p1, p2, cur)
    # p1 증가 차례가 되었는데
    # S를 넘었으면 p2 를 줄여가야함
    if cur >= S:
        while p1 < p2: # cur >= S일 때 p2를 왼쪽으로
            p2 -= 1
            length -= 1
            cur -= numbers[p2]
            if cur >= S:
                if ans > length:
                    ans = length
            else:
                break
    else: # cur < S일 때 p2 를 오른쪽으로
        while p2 < N-1:
            p2 += 1
            length += 1
            cur += numbers[p2]
            if cur >= S:
                if ans > length:
                    ans = length
                break

    cur -= numbers[p1]

    if p1 == p2:
        p1 += 1
        p2 += 1
        if p1 < N:
            cur = numbers[p1]
            length = 1
    else:
        p1 += 1
        length -= 1

if ans == 100000:
    print(0)
else:
    print(ans)        
"""
