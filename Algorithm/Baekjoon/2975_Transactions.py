"""
2975 Transactions

수학, 구현, 사칙연산
문제가 영어인 것 뿐 브론즈 3 중에서 쉬운 편인 것 같다.
"""

while True:
    money, op, value = input().split()
    if money == '0' and value == '0': break
    money = int(money)
    value = int(value)
    if op == 'W':
        money -= value
        if money < -200:
            print("Not allowed")
        else:
            print(money)
    else:
        print(money + value)
