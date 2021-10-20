"""
20470 최대공약수
"""
def gcd(a, b):
    return gcd(b, a%b) if b else a

n, d = map(int, input().split())
a = list(map(int, input().split()))

g = 0
ans = []
for i in range(n):
    temp = gcd(g, a[i])
    if temp % d == 0:
        g = temp
        ans.append(a[i])

if g == d:
    print(len(ans))
    print(*ans)
else:
    print(-1)
