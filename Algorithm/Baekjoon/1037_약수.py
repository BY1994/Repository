"""
1037 약수
"""

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[0] * numbers[-1])
