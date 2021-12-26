"""
2512 예산
"""

import sys

def check(n, M):
    ans = 0
    for i in towns:
        if i > n:
            ans += n
        else:
            ans += i
    if ans <= M:
        return True
    return False

def binary_search(n):
    left = 1
    right = max(towns) #100000
    mid = 0
    ans = 0

    while left <= right:
        mid = (left+right)//2
        if check(mid, n) == True:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

N = int(input())
towns = list(map(int, sys.stdin.readline().split()))
M = int(input())

print(binary_search(M))
