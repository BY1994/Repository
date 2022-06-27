"""
2616 소형기관차

for 문을 돌 때 앞에서부터 탐색하면 다음으로 건너뛰기 어려운 게 맞나?

브루트포스로 하면 3중 포문이라 시간 안에 들어올 수 없음

계속 틀렸던 이유
다른 정답 답안은 for (int i = 1; i <= 3; i++) for (int j = i*m; j<= n; j++) 로만 돌길래
이렇게 안해서 어디선가 반례가 생긴 줄 알았는데 아니었다.
DP 의 가장 위를 max 를 취해주지 않았기 때문이었다.

반례 만들기 (랜덤 생성)
9
26 6 25 18 18 18 4 44 68
1
정답 = 26 + 44 + 68 = 138

질문 게시판의 반례 만들기 (랜덤 생성)
https://www.acmicpc.net/board/view/16440
8
43 5 21 88 54 86 92 59
2
정답 400
틀린 답 384
"""

# 0 번은 무조건 아무것도 없다가 나를 추가하는 케이스라고 잘못 생각했는데,
# 나를 추가하지 않고 이전에 0 번인 거 그대로 가져오는 케이스도 고려해야한다
# 이걸 안 했더니 최대값이 덮어씌워져버렸다.

N = int(input())
trains = list(map(int, input().split()))
limit = int(input())

DP = [[0 for i in range(3)] for j in range(N+1)]
prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + trains[i-1]

# for 문을 limit 부터 돌려면 DP[i-limit] 때문에 처음 거 하나는 구해야함
DP[limit-1][0] = prefix[limit] - prefix[0]

for i in range(limit, N):
    cur = prefix[i+1] - prefix[i+1-limit]
    DP[i][0] = max(DP[i-1][0], cur)
    DP[i][1] = max(DP[i-1][1], DP[i-limit][0] + cur)
    DP[i][2] = max(DP[i-1][2], DP[i-limit][1] + cur)

print(DP[N-1][2])


# input / output 생성
"""
from random import randrange
fread = open("2616_input.txt", 'w')
fwrite = open("2616_output.txt", 'w')
for tc in range(100):
    N = randrange(3,11)
    fread.write(f'{N}\n')
    trains = []
    for i in range(N):
        trains.append(randrange(1,101))
    fread.write(f"{' '.join(str(x) for x in trains)}\n")
    limit = randrange(1,N//3+1)
    fread.write(f'{limit}\n')

    # 비교 코드: https://velog.io/@kimdukbae/BOJ-2616-%EC%86%8C%ED%98%95%EA%B8%B0%EA%B4%80%EC%B0%A8-Python
    # 구간합 계산
    S = [0]
    value = 0
    for t in trains:
        value += t
        S.append(value)

    dp = [[0] * (N + 1) for _ in range(4)]

    # 점화식을 이용해 최댓값 탐색
    for n in range(1, 4):
        for m in range(n * limit, N + 1):
            # n = 1일 때 선택한 객차가 없으므로
            # 전에 계산한 구간합과 현재 계산하는 구간합 중 최댓값을 계산해 갱신해준다.
            if n == 1:
                dp[n][m] = max(dp[n][m - 1], S[m] - S[m - limit])

            # 점화식
            else:
                dp[n][m] = max(dp[n][m - 1], dp[n - 1][m - limit] + S[m] - S[m - limit])
            # print_dp(dp)

    fwrite.write(f"{dp[3][N]}\n")
fread.close()
fwrite.close()
"""

# 채점 프로그램
"""
from random import randrange
for tc in range(1):
    #N = randrange(3,11)
    #trains = []
    #for i in range(N):
    #    trains.append(randrange(1,101))
    #limit = randrange(1,N//3+1)
    N = 9
    trains = [26, 6, 25, 18, 18, 18, 4, 44, 68]
    limit = 1

    DP = [[0 for i in range(3)] for j in range(N+1)]
    prefix = [0] * (N+1)

    for i in range(1,N+1):
        prefix[i] = prefix[i-1] + trains[i-1]

    DP[limit-1][0] = prefix[limit] - prefix[0]

    for i in range(limit, N):
        cur = prefix[i+1] - prefix[i+1-limit]
        DP[i][0] = max(DP[i-1][0], cur)
        DP[i][1] = max(DP[i-1][1], DP[i-limit][0] + cur)
        DP[i][2] = max(DP[i-1][2], DP[i-limit][1] + cur)

    print("# my", DP[N-1][2])

    # 비교 코드: https://velog.io/@kimdukbae/BOJ-2616-%EC%86%8C%ED%98%95%EA%B8%B0%EA%B4%80%EC%B0%A8-Python
    # 구간합 계산
    S = [0]
    value = 0
    for t in trains:
        value += t
        S.append(value)

    dp = [[0] * (N + 1) for _ in range(4)]

    # 점화식을 이용해 최댓값 탐색
    for n in range(1, 4):
        for m in range(n * limit, N + 1):
            # n = 1일 때 선택한 객차가 없으므로
            # 전에 계산한 구간합과 현재 계산하는 구간합 중 최댓값을 계산해 갱신해준다.
            if n == 1:
                dp[n][m] = max(dp[n][m - 1], S[m] - S[m - limit])

            # 점화식
            else:
                dp[n][m] = max(dp[n][m - 1], dp[n - 1][m - limit] + S[m] - S[m - limit])
            # print_dp(dp)

    print("# answer", dp[3][N])
"""

# 틀렸습니다
# 무조건 3대는 배치하는 거로 수정
"""
N = int(input())
trains = list(map(int, input().split()))
limit = int(input())

DP = [[0 for i in range(3)] for j in range(N+1)]
prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + trains[i-1]

DP[limit-1][0] = prefix[limit] - prefix[0]

for i in range(limit, N):
    cur = prefix[i+1] - prefix[i+1-limit]
    DP[i][0] = cur
    DP[i][1] = max(DP[i-1][1], DP[i-limit][0] + cur)
    DP[i][2] = max(DP[i-1][2], DP[i-limit][1] + cur)

print(DP[N-1][2])
"""

# 틀렸습니다
"""
N = int(input())
trains = list(map(int, input().split()))
limit = int(input())

DP = [[0 for i in range(3)] for j in range(N+1)]
prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + trains[i-1]

DP[limit-1][0] = prefix[limit] - prefix[0]

for i in range(limit, N):
    cur = prefix[i+1] - prefix[i+1-limit]
    DP[i][0] = cur
    DP[i][1] = max(DP[i-1][1], DP[i-limit][0] + cur)
    DP[i][2] = max(DP[i-1][2], DP[i-limit][1] + cur)

print(max(DP[N-1]))
"""

