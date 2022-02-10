"""
11134 쿠키애호가
"""

for _ in range(int(input())):
    n, c = map(int, input().split())
    print(n//c + (1 if n%c else 0))
