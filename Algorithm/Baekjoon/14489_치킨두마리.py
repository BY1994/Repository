"""
14489 치킨 두마리

int 범위 벗어나지 않음
"""

A, B = map(int, input().split())
C = int(input())
if A + B < 2 * C:
    print(A+B)
else:
    print(A+B - 2*C)
