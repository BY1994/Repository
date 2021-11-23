"""
10829 이진수 변환
"""

import sys
sys.setrecursionlimit(10000)

ans = []
def dec2bin(n):
    if n <= 1:
        ans.append(n)
    else:
        ans.append(n % 2)
        return dec2bin(n//2)

dec2bin(int(input()))
print(*ans[::-1], sep="")
