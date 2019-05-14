"""
2750 BOJ 수 정렬하기

2019.05.14 PBY
"""


N = int(input())
numbers = [0] * N

for i in range(N):
    numbers[i] = int(input())

numbers.sort()

for i in range(N):
    print(numbers[i])
