def backtracking(cur, depth):
    global N, M

    if depth == M:
        print(*ans)
        return

    for i in range(cur+1, N):
        ans[depth] = number[i]
        backtracking(i, depth+1)

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
ans = [0]*M
for i in range(N):
    ans[0] = number[i]
    backtracking(i, 1)
