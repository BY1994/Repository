"""
18310 안테나

중앙값의 성질

N//2 해버리면 안 됨
(N-1)//2 해야함
"""

N = int(input())
houses = list(map(int, input().split()))
houses.sort()

print(houses[(N-1)//2])
