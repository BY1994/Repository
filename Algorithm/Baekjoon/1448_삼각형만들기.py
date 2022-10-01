"""
1448 삼각형 만들기

정렬, 그리디, 기하학

그리디인 이유는 정렬된 결과가 a b c 일 때 a 가 b+c 보다 커서
다른 숫자를 보려고 할 때 b 나 c 보다 더 오른쪽에 있으면 무조건 작아지기 때문에
a 에 맞는 삼각형을 만들 순 없다. 그래서 그리디가 된다! ★
"""

import sys

input = sys.stdin.readline
N = int(input())
straw = []
for i in range(N):
    straw.append(int(input()))
straw.sort(reverse=True)
for i in range(N-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        print(straw[i] + straw[i+1] + straw[i+2])
        break
else:
    print(-1)
