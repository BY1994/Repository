"""
2501 약수 구하기
"""

N, K = map(int, input().split())

cur = 0
ans = 0
for i in range(1, N+1):
    if N % i == 0:
        cur += 1
        if cur == K:
            ans = i
            break
print(ans)
