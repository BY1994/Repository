"""
2506 점수계산

다른 사람들 코드를 보니 cur 0 따로 체크 안 하고
cur = (cur + 1) * input 값으로 해서
0인지 1인지도 한 번에 고려될 수 있도록 했다
"""

N = int(input())
scores = map(int, input().split())

total = 0
cur = 0
for score in scores:
    if score:
        cur += score
        total += cur
    else:
        cur = 0

print(total)

# https://www.acmicpc.net/source/11421702
"""
i=input;i();d=r=0
for _ in i()[::2]:d=(d+1)*int(_);r+=d
print(r)
"""
