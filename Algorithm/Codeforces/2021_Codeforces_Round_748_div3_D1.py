def gcd(a, b):
    return gcd(b, a%b) if b else a

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    g = 0
    for i in range(1, N):
        d = A[i] - A[0]
        if d < 0: d = -d # abs
        g = gcd(d, g)
    if g == 0:
        g= -1
    print(g)
