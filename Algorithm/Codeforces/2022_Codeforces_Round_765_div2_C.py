n, l, k = map(int, input().split())
d = list(map(int, input().split()))
a = list(map(int, input().split()))
d.append(l)
ans = 0

for i in range(k):
    dist = -1
    ind = 0
    cur = 0
    for j in range(1, n):
        if a[j] <= a[j-1]: continue
        cur = (d[j+1]-d[j])*a[j]
        if cur > dist:
            dist = cur
            ind = j

    if dist < 0: break
    n -= 1
    a = a[:ind]+a[ind+1:]
    d = d[:ind]+d[ind+1:]

for i in range(n):
    ans += (d[i+1]-d[i])*a[i]

print(ans)
