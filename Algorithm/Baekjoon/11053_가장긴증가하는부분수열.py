"""
11053 가장 긴 증가하는 부분 수열

반례
https://www.acmicpc.net/board/view/75156
"100%에서 틀린다면 데이터가 가장 작은 경우가 많습니다."

1
10
내 답 0

ans 초기화 0 아니라 1이어야함

DP 를 이용해서 도전했는데,
LIS 알고리즘을 보니 코드 내용이 동일하다.
단, 이 경우 N^2 시간 복잡도를 갖지만,
여기에 이분탐색을 더하면 NlogN 이 된다고 한다.
https://chanhuiseok.github.io/posts/algo-49/
"""

N = int(input())
A = list(map(int, input().split()))
DP = [1 for i in range(N)]
ans = 1
for start in range(N):
    for compare in range(start+1,N):
        if A[compare] > A[start]:
            if DP[compare] <= DP[start]:
                DP[compare] = DP[start] + 1
                if DP[compare] > ans:
                    ans = DP[compare]

print(ans)
