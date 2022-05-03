"""
18244 변형 계단수

1562 번 계단수 문제를 풀고 도전해본 문제
- if i > 0: elif i < 9: 이렇게 잘못 써서 예제도 틀림
- 문제 잘못 이해함 3번 넘으면 안 됨!!

입출력 예제
1 -> 10
2 -> 18
3 -> 34
4 -> 50
"""

N = int(input())
DP = [[[0 for i in range(4)] for j in range(10)] for k in range(N+1)]
# -2 -1 1 2

if N == 1:
    print(10)
else:
    for i in range(10):
        if i > 0: # 0 은 증가는 없음
            DP[2][i][2] = 1
        if i < 9: # 9 는 감소는 없음
            DP[2][i][1] = 1

    for i in range(3, N+1):
        for j in range(10):
            if j > 0: # 0 은 증가는 없음 (-2, -1 -> +1 될 수 있음)
                DP[i][j][2] += DP[i-1][j-1][0] + DP[i-1][j-1][1]
                DP[i][j][2] %= 1000000007
                DP[i][j][3] += DP[i-1][j-1][2] # +1 -> +2
                DP[i][j][3] %= 1000000007
                
            if j < 9: # 9 는 감소는 없음 (+1, +2 -> -1 될 수 있음)
                DP[i][j][1] += DP[i-1][j+1][2] + DP[i-1][j+1][3]
                DP[i][j][1] %= 1000000007
                DP[i][j][0] += DP[i-1][j+1][1] # -1 -> -2
                DP[i][j][0] %= 1000000007

    ans = 0
    for i in range(10):
        ans += sum(DP[N][i])
        ans %= 1000000007

    print(ans)

# 잘못된 풀이
# 3번 넘으면 안 됨
# 이렇게 하면 1, 2, 3까지는 맞고 4 부터 잘못된 답 나옴
"""
N = int(input())
DP = [[[0 for i in range(6)] for j in range(10)] for k in range(N+1)]
# -3 -2 -1 1 2 3

if N == 1:
    print(10)
else:
    for i in range(10):
        if i > 0: # 0 은 증가는 없음
            DP[2][i][3] = 1
        if i < 9: # 9 는 감소는 없음
            DP[2][i][2] = 1

    for i in range(3, N+1):
        for j in range(10):
            if j > 0: # 0 은 증가는 없음 (-3, -2, -1 -> +1 될 수 있음)
                DP[i][j][3] += DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]
                DP[i][j][3] %= 1000000007
                DP[i][j][4] += DP[i-1][j-1][3] # +1 -> +2
                DP[i][j][4] %= 1000000007
                DP[i][j][5] += DP[i-1][j-1][4] # +2 -> +3
                DP[i][j][5] %= 1000000007
                
            if j < 9: # 9 는 감소는 없음 (+1, +2, +3 -> -1 될 수 있음)
                DP[i][j][2] += DP[i-1][j+1][3] + DP[i-1][j+1][4] + DP[i-1][j+1][5]
                DP[i][j][2] %= 1000000007
                DP[i][j][1] += DP[i-1][j+1][2] # -1 -> -2
                DP[i][j][1] %= 1000000007
                DP[i][j][0] += DP[i-1][j+1][1] # -2 -> -3
                DP[i][j][0] %= 1000000007

    ans = 0
    for i in range(10):
        ans += sum(DP[N][i])
        ans %= 1000000007

    print(ans)
"""
