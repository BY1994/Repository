"""
17284 Vending Machine

2019.06.26 PBY 최초작성
"""

money = 5000
drink = [0, 500, 800, 1000]
buttons = list(map(int, input().split()))
for b in buttons:
    money -= drink[b]
print(money)
