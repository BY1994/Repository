"""
3512 Flat

틀린 이유
bedroom 및 balcony 가 여러 개 입력될 수 있기 때문에
(예시에 bathroom 이 여러 개 입력된 게 보임)
 = a 가 아니라 += a 로 입력해야 맞다
"""

n, c = map(int, input().split())
total = 0
bedroom = 0
balcony = 0
for i in range(n):
    a, t = input().split()
    a = int(a)
    if t == "bedroom":
        bedroom += a
    elif t == "balcony":
        balcony += a
    total += a
print(total)
print(bedroom)
print((total - balcony/2)*c)
