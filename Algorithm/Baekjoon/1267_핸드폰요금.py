"""
1267 핸드폰 요금

기초 사칙연산
"""

N = int(input())
calls = map(int, input().split())
Y, M = 0, 0
for call in calls:
    Y += (call // 30)*10 + 10
    M += (call // 60)*15 + 15

if Y < M:
    print("Y", Y)
elif Y > M:
    print("M", M)
else:
    print("Y M", Y)
