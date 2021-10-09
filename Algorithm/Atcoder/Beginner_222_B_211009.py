"""
atcoder
#b
"""
N, P = map(int, input().split())
ans = 0
scores = map(int, input().split())
for i in scores:
    if i < P:
        ans += 1
print(ans)
