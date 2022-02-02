"""
24420 Piano Competition
"""

N = int(input())
ans = 0
_min = 101
_max = 0
A = list(map(int, input().split()))
for i in A:
    ans += i
    if _min > i:
        _min = i
    if _max < i:
        _max = i

print(ans - _min - _max)
