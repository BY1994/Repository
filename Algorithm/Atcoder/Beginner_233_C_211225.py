def dfs(cur, depth):
    global N, X, ans
    if depth >= N:
        if cur == X:
            ans += 1
        return

    for i in bags[depth]:
        if cur * i > X: break
        dfs(cur * i, depth+1)

N, X = map(int, input().split())
bags = []
for _ in range(N):
    L = list(map(int, input().split()))
    bags.append(sorted(L[1:]))

ans = 0
for i in bags[0]:
    if i > X: break
    dfs(i, 1)
print(ans)

"""
N, X = map(int, input().split())
check = [0] * 100010
for _ in range(N):
    L = list(map(int, input().split()))
    for i in range(L[0]):
        check[L[1+i]] += 1

ans = 0
for i in range(1, 100001):
    if check[i] >= 1:
        if X % i == 0:
            ans += check[i]*check[X // i]

print(ans // 2)
"""
