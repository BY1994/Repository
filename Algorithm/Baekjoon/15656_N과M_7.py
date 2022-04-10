"""
15656 N과 M 7
"""

def backtracking(depth):
    global N, M

    if depth == M:
        print(*ans)
        return

    for i in range(N):
        ans[depth] = arr[i]
        backtracking(depth+1)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = [0] * M
arr.sort()

for i in range(N):
    ans[0] = arr[i]
    backtracking(1)
