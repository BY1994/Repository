"""
11053 가장 긴 증가하는 부분 수열 (not submitted)
"""
N = int(input())
A = list(map(int, input().split()))
DP = [1 for i in range(N)]
ans = 0
for start in range(N):
    for compare in range(start+1,N):
        if A[compare] > A[start]:
            if DP[compare] <= DP[start]:
                DP[compare] = DP[start] + 1
                if DP[compare] > ans:
                    ans = DP[compare]

print(ans)
