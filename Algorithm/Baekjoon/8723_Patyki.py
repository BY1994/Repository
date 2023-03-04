"""
8723 Patyki
"""

a, b, c = map(int, input().split())
_max = max(a, max(b, c))
if a == b and b == c:
    print(2)
elif a**2 + b**2 + c**2 - _max**2 == _max**2:
    print(1)
else:
    print(0)
