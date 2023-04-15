"""
2484 주사위 네개

구현, 많은 조건 분기

설계를 대충하고 코드를 짜기 시작했더니 중간에 수정이 많이 이루어짐
원래는 counts 배열로 1, 2, 3, 4 번 나왔는지 여부를 세서 관리하려고 했는데,
그러면 그 때의 주사위 눈 값도 따로 관리해야해서 다음과 같이 간단하게 if 조건으로 구현하였다.
"""

import sys
input = sys.stdin.readline

dices = [[0 for i in range(7)] for j in range(1000)]
max_money,cur_money = 0, 0
for n in range(int(input())):
    a, b, c, d = map(int, input().split())
    dices[n][a] += 1
    dices[n][b] += 1
    dices[n][c] += 1
    dices[n][d] += 1
    already, alvalue = 0, 0
    for dice in range(1,7):
        if dices[n][dice] == 4:
            cur_money = 50000 + dice*5000
            break
        elif dices[n][dice] == 3:
            cur_money = 10000 + dice*1000
            break
        elif dices[n][dice] == 2:
            if already == 0:
                already = 1
                alvalue = dice
            else:
                cur_money = 2000 + alvalue*500 + dice*500
                break
    else:
        if already:
            cur_money = 1000 + alvalue*100
        else:
            cur_money = max(a,b,c,d) * 100

    if cur_money > max_money:
        max_money = cur_money

print(max_money)
