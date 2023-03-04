"""
2476 주사위 게임

a != b 인 경우
a == c 라면 b == c 일 수는 없다. 그러면 a == b가 되어버리는 것이기 때문에
a == c 이거나 b == c인 경우로 나뉘어진다.
"""

max_prize = 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b:
        if b == c:
            max_prize = max(max_prize, 10000 + a * 1000)
        else:
            max_prize = max(max_prize, 1000 + a * 100)
    else: # a != b
        if a == c:
            max_prize = max(max_prize, 1000 + a * 100)
        elif b == c:
            max_prize = max(max_prize, 1000 + b * 100)
        else:
            max_prize = max(max_prize, max(a, max(b, c))*100)
print(max_prize)

    
