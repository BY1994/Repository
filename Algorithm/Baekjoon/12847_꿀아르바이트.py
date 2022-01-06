"""
12847 꿀 아르바이트

엄청 간단한 sliding window 문제

python 시간 1등과 풀이가 동일
"""

import sys

n, m = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

cur = 0
for i in range(m):
    cur += t[i]

ans = cur

for i in range(n-m):
    cur -= t[i]
    cur += t[i+m]

    if ans < cur:
        ans = cur

print(ans)
