"""
22938 백발백준하는 명사수

기하학
원의 반지름의 합과 좌표 사이 거리 비교
"""

X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

if (R1 + R2)**2 > (X1-X2)**2 + (Y1-Y2)**2:
    print("YES")
else:
    print("NO")
