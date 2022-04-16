"""
2748 피보나치 수 2

재귀는 시간초과

n 최대인 90 을 넣었을 때 답
2880067194370816120
"""

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

# 시간초과
# 90 써보면 답 안 나옴
"""
def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))
"""
