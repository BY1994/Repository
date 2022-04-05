def gcd(a, b):
    return gcd(b, a%b) if b else a

A, B = map(int, input().split())
g = gcd(A, B)
print(g)
print(A*B // g)
