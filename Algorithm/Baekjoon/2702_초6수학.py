"""
2702 초6 수학
최대공약수, 최소공배수 구하기 - gcd
"""

def gcd(a, b):
    return gcd(b, a%b) if b else a

for _ in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(a//g*b, g)
