
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

N = int(input())
a = list(map(int, input().split()))

g = a[0]
for i in range(1,N):
    g = gcd(g, a[i])

ans = 0
for i in a:
    cur = i//g
    while cur > 1:
        if cur % 2 == 0:
            cur //= 2
            ans += 1
        elif cur % 3 == 0:
            cur //= 3
            ans += 1
        else:
            ans = -1
            break
    if ans == -1:
        break

print(ans)
