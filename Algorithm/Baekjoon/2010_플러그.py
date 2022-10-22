"""
2010 플러그

단순 사칙연산
"""
import sys
input = sys.stdin.readline

n = int(input())
ans = int(input())
for i in range(n-1):
    ans += int(input()) - 1
print(ans)
