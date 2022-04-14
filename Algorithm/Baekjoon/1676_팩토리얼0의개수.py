"""
1676 팩토리얼 0의 개수
"""

numbers_2 = [0] * 501
numbers_5 = [0] * 501

for i in range(1,501):
    if i % 2 == 0:
        numbers_2[i] = numbers_2[i//2]+1
    if i % 5 == 0:
        numbers_5[i] = numbers_5[i//5]+1

N = int(input())
print(min(sum(numbers_2[:N+1]), sum(numbers_5[:N+1])))
