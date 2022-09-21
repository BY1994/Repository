"""
25370 카드 숫자 곱의 경우의 수

9^7 = 4,782,969

7개 중복해서 고르는 경우 = 5040
"""

def select_card(depth, total):
    global n, count
    if depth == n:
        if numbers[total] == 0:
            numbers[total]  = 1
            count += 1
        return

    for i in range(1, 10):
        select_card(depth+1, total*i)

n = int(input())
numbers = [0]*5000000
count = 0

for i in range(1, 10):
    select_card(1, i)

print(count)
