"""
1448 삼각형 만들기

정렬, 그리디, 기하학
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
