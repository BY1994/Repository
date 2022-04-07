def gcd(a, b):
    return gcd(b, a%b) if b else a

for tc in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//gcd(A, B))
