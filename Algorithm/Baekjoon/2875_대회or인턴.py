"""
2875 대회 or 인턴

수학 계산 문제
"""

N, M, K = map(int, input().split())

total = N + M
c = min(N//2, M) # 남, 여 조합 최소쌍
left = total - 3*c
K -= left

if K <= 0:
    print(c)
else:
    i = K // 3
    i += 1 if K % 3 else 0
    print(c - i)
