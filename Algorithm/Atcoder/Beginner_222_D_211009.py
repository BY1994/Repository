"""
atcoder
#4
"""
# maybe time exceed
def dfs(n, value):
    if n == N-1:
        return 1
    ans = 0
    for i in range(b[n+1]-a[n+1]+1):
        if i >= value:
            ans += dfs(n+1, i)
    ans %= 998244353
    return ans

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for i in range(b[0]-a[0]+1):
    ans += dfs(0, i)
    ans %= 998244353

print(ans)

# Wrong
"""
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 1

for i in range(N):
    ans *= (b[i] - a[i] + 1)
    ans %= 998244353

print(ans)
"""
