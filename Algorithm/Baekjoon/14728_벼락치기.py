"""
14728 벼락치기

DP 풀 때 [아이템][무게] = 최대 가치

냅색 문제 코드 참고
https://chanhuiseok.github.io/posts/improve-6/

# 틀리고 나서 발견한 질문 게시판
https://www.acmicpc.net/board/view/51349
일차원 배열을 이용할 경우에는 dp[k:t+1] 구간만 업데이트해주면 되는게 맞지만,
이차원 배열로 매번마다 새로운 배열을 채울 경우에는 dp[i][k:t+1] 구간만 업데이트하면, 
dp[i][:k] 구간은 채워지지 않기 때문에 (dp[i-1][:k] 로 채워줘야 하는데 0인 상태로 남아있기 때문에)
잘못된 값이 나올 수 밖에 없습니다.
"""

N, T = map(int, input().split())
chapters = []
DP = [[0 for i in range(10001)] for j in range(100)]
for i in range(N):
    K, S = map(int, input().split())
    chapters.append([K,S])

for i in range(N):
    for j in range(T+1):
        if j >= chapters[i][0]:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-chapters[i][0]]+chapters[i][1])
        else:
            DP[i][j] = DP[i-1][j]

print(max(DP[N-1]))

# 틀렸습니다.
"""
N, T = map(int, input().split())
chapters = []
DP = [[0 for i in range(10001)] for j in range(100)]
for i in range(N):
    K, S = map(int, input().split())
    chapters.append([K,S])

for i in range(N):
    for j in range(chapters[i][0], T):
        DP[i][j] = max(DP[i-1][j], DP[i-1][j-chapters[i][0]]+chapters[i][1])

print(max(DP[N-1]))
"""
