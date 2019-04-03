"""
10952 A+B - 5

2019.04.02 PBY 최초작성
"""


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)
