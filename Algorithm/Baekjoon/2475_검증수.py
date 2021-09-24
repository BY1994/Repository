"""
2475 검증수

"""

total = 0
numbers = list(map(int, input().split()))
for i in range(5):
    total += numbers[i]*numbers[i]
print(total % 10)

# 숏코딩 참고
"""
L = [x**2 for x in map(int,input().split())]
print(sum(L)%10)
"""

# 나보다 빠른 코드
"""
a = list(map(int, input().split()))
ab = 0
for i in a:
    ab += i ** 2

print(ab % 10)
"""
