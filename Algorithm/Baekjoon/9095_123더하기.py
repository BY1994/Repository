"""
9095 1, 2, 3 더하기

"""
memo = [0] * 20

def dp(n):
    if n == 1:
        return 1
    if n == 2: # 1+1 / 2
        return 2
    if n == 3:
        return 4 # 1+1+1 / 2+1 / 1+2 / 3

    if memo[n]:
        return memo[n]

    memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return memo[n]

for t in range(int(input())):
    n = int(input())
    print(dp(n))


# 다른 사람들 코드
"""
import sys
r = sys.stdin.readline

arr = [0] * 11
arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
for _ in range(int(r())):
    num = int(r())
    print(arr[num])
"""

"""
N = int(input())
arr=[1,2,4]
for i in range(4,11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])
"""
