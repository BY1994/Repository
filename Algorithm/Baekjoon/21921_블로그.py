"""
21921 블로그
"""

import sys

N, X = map(int, sys.stdin.readline().split())
blog = list(map(int, sys.stdin.readline().split()))

mnum = 1
mval = 0

cur = 0
for i in range(X):
    cur += blog[i]

mval = cur

for i in range(N-X):
    cur -= blog[i]
    cur += blog[i+X]

    if mval < cur:
        mnum = 1
        mval = cur
    elif mval == cur:
        mnum += 1

if mval > 0:
    print(mval)
    print(mnum)
else:
    print("SAD")
