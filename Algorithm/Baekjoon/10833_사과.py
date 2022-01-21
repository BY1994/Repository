"""
10833 사과
"""

N = int(input())
ans = 0
for _ in range(N):
    student, apple = map(int, input().split())
    ans += apple % student

print(ans)
