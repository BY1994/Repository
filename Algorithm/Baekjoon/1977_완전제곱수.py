"""
1977 완전제곱수
"""

M = int(input())
N = int(input())

A = [0 for i in range(100001)]

for i in range(1, 101): # 100 으로 해서 틀렸음
    A[i*i] = 1

_sum = 0
_min = 100001
for i in range(M, N+1):
    if A[i] == 1:
        _sum += i
        _min = min(_min, i)

if _min == 100001:
    print(-1)
else:
    print(_sum)
    print(_min)
