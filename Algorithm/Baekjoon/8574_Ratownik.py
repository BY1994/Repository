"""
8574 Ratownik

기하학
구할 수 있는 원 범위를 넘어섰는지 확인
(k 미터까지 구할 수 있다고 함. k 미터 모으면 원)
"""

ans = 0
n, k, x, y = map(int, input().split())
for i in range(n):
    x1, y1 = map(int, input().split())
    if (x1 - x)**2 + (y1 - y)**2 > k**2:
        ans += 1
print(ans)
