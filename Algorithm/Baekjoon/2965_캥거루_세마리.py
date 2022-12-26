"""
2965 캥거루 세마리

수학
분류가 그리디가 아닌가?
"""

A, B, C = map(int, input().split())
print(max(B-A, C-B)-1)
