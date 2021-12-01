"""
1182 부분수열의 합
"""

def dfs(cur, depth, s):
    global ans

    if s == S:
        ans += 1

    if depth > N:
        return

    for i in range(cur+1, N):
        dfs(i, depth+1, s + numbers[i])

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
# visited = [0] * N => 순서 상관 없는 경우 visited 안 필요

ans = 0
for i in range(N):
    dfs(i, 1, numbers[i])

print(ans)
