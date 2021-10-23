"""
Atcoder 224
"""
# runtime error (up down vs left right order wrong!)
def check(l, r, u, d):
    return A[u][l] + A[d][r] <= A[u][r] + A[d][l]

h, w = map(int, input().split())
A = []
for _ in range(h):
    A.append(list(map(int, input().split())))

# l 잡고, r를 넓혀가면서
def solve():
    for l in range(w):
        for r in range(l+1, w): # +1 missing (runtime error?)
            for u in range(h):
                for d in range(u+1, h):
                    if check(l, r, u, d) == False:
                        return False
    return True

print(("No", "Yes")[solve()])
