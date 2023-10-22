"""
3578 Holes

greedy

0이면 1
1이면 0
구멍이 필요하면 무조건 4와 8의 조합

숏코딩하려면 아래 if 문 2개 2개씩 합칠 수 있음
1-n 으로 식을 만들 수 있고
'4'*(n%2) + '8'*(n//2) 로 식을 합칠 수 있음
"""

n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(0)
elif n%2 == 0:
    print('8'*(n//2))
else:
    print('4' + '8'*(n//2))
