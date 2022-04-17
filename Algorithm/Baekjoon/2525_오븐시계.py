"""
2525 오븐 시계

수학

정보올림피아드 초등부 1번
"""

A, B = map(int, input().split())
C = int(input())

B += C
A = A + (B // 60)
print(A%24, B%60)
