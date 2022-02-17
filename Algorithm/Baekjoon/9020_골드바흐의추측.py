"""
9020 골드바흐의 추측
"""

import sys
input = sys.stdin.readline

sieve = [0]*10001

for i in range(2, 10001):
    for j in range(2, 10001):
        if i*j > 10000:
            break
        sieve[i*j] = 1

for tc in range(int(input())):
    n = int(input())

    ans = 0
    for i in range(n//2, 1, -1):
        if sieve[i] == 0 and sieve[n-i] == 0:
            ans = i
            break
    print(ans, n-ans)
