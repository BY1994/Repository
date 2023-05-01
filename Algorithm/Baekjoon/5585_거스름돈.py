"""
5585 거스름돈

그리디
동전 문제이지만 배수인 경우 그리디가 된다.
"""
money = 1000 - int(input())
print(money//500 + (money%500)//100 + (money%100)//50 + (money%50)//10 + (money%10)//5 + (money%5))
