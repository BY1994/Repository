"""
17608 막대기

stack
"""

import sys
input = sys.stdin.readline

stick = []
N = int(input())
for i in range(N):
    stick.append(int(input()))

ans = 0
last = 0
for i in range(N-1, -1, -1):
    if stick[i] > last:
        ans += 1
        last = stick[i]

print(ans)
