"""
9657 돌 게임 3

돌을 1개 3개 4개 가져갈 수 있음

질문검색 게시판을 보면
베스킨라빈스 31 필승 전략같이
계산이 가능하다고 한다.
"""

dp = [[0] * 1001 for _ in range(2)]
N = int(input())

# 0 상근 턴 1 창영 턴
# 1 상근 윈 2 창영 윈
dp[0][1] = 1
dp[1][1] = 2

dp[0][2] = 2
dp[1][2] = 1

dp[0][3] = 1
dp[1][3] = 2

dp[0][4] = 1
dp[1][4] = 2

# 자기 턴에 최선을 다한 결과

for i in range(5, N+1):
    res = 2
    if dp[1][i-1] == 1: # 내 턴에서 1, 3, 4를 빼면 상태턴으로 바뀜
        res = 1
    if dp[1][i-3] == 1:
        res = 1
    if dp[1][i-4] == 1:
        res = 1
    dp[0][i] = res

    res = 1
    if dp[0][i-1] == 2:
        res = 2
    if dp[0][i-3] == 2:
        res = 2
    if dp[0][i-4] == 2:
        res = 2
    dp[1][i] = res

print("SK" if dp[0][N] == 1 else "CY")


# 숏코딩
# https://www.acmicpc.net/source/14284537
"""
print('CY'if int(input())%7in[0,2]else'SK')
"""
