"""
Atcoder 226 D
"""
def gcd(a, b):
    return gcd(b, a%b) if b else a

N = int(input())

possible = []

all_comb = []
for _ in range(N):
    a, b = map(int, input().split())
    all_comb.append([a, b])

for i in range(N):
    ai, bi = all_comb[i]
    for j in range(i+1, N):
        aj, bj = all_comb[j]
        diffa, diffb = ai -aj, bi-bj
        g = gcd(diffa, diffb)
        possible.append((diffa//g, diffb//g))
        possible.append((-1*diffa//g, -1*diffb//g))

print(len(set(possible)))
