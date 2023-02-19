"""
6322 직각 삼각형의 두 변

기하학, 피타고라스의 정리
a, b, c(빗변) 중 한 값을 모를 때 그 값 구하기 

###
round 처리 때문에 오류가 생긴 건 줄 알았는데
한참 알고 보니 a = 이라고 써야하는 걸 b = 이라고 오타낸 것 뿐이었다.

cf) round(2.5)
"""

import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

TC = 0
while True:
    TC += 1
    a, b, c = map(int, input().split())
    if a == 0:
        break
    print(f'Triangle #{TC}')
    if c == -1:
        print(f'c = {round(decimal.Decimal((a**2 + b**2)**(1/2)),3):.3f}')
    elif b == -1:
        if a >= c:
            print(f'Impossible.')
        else:
            print(f'b = {round(decimal.Decimal((c**2 - a**2)**(1/2)),3):.3f}')
    else:
        if b >= c:
            print(f'Impossible.')
        else:
            print(f'a = {round(decimal.Decimal((c**2 - b**2)**(1/2)),3):.3f}')
    print()
