"""
11
12
21

22
23
32

1 x
  1  x
     1  x
        1 x
          1
          2
        2 1
          2
          3
     2  1 x
          1
          2
        2 1
          2
          3
        3`
  2  1
     2
     3

2 1
  2
  3
3 2
  3
  4
4 3
  4
  5
5 4
  5
  6
8 7
  8
  9
9 8
  9
  x
1자리면 9
2자리면 9 * 3 - 1 - 1 = 25
3자리면
1 x x
  1 x
    1
    2
  2 1
    2
    3
2 1 x
    1
    2
  2 1
    2
    3
  3 1
    2
    3
3 2 1
    2
    3
  3 2
    3
    4
  4 3
    4
    5
4 3 2
    3
    4
  4 3
    4
    5

8 7 6
    7
    8
  8 7
    8
    9
  9 8
    9
    x

9 8 7
    8
    9
  9 8
    9
    x
  x
71
"""
# 맨 앞자리 1 일 때
# 1 *1

# 맨 앞자리 1일 떄
# 1 x *3 존재하지 않는 1보다 작은 수
# 두번째 자리 1일 때
# 맨 앞이 1이거나 2인 경우가 있음
# 1 1 *1 (마지막 자리)
# 2 1 *1 (마지막 자리)

"""
N = int(input())
DP = [[0 for i in range(9)] for j in range(N)]
for i in range(9):
    DP[0][i] = 1

for i in range(N-1):
    for j in range(9):
        # smaller
        if j - 1 >= 0:
            DP[i+1][j-1] += DP[i][j]
            DP[i+1][j-1] %= 998244353
        # same
        DP[i+1][j] += DP[i][j]
        DP[i+1][j] %= 998244353
        # bigger
        if j + 1 <= 8:
            DP[i+1][j+1] += DP[i][j]
            DP[i+1][j+1] %= 998244353

print(sum(DP[N-1])%998244353)
"""

# pypy 제출 통과

N = int(input())
DP = [[0 for i in range(9)] for j in range(N)]
for i in range(9):
    DP[0][i] = 1

for i in range(1, N):
    for j in range(9):
        if j > 0:
            DP[i][j] += DP[i-1][j-1]
        if j < 8:
            DP[i][j] += DP[i-1][j+1]
        DP[i][j] += DP[i-1][j]
        DP[i][j] %= 998244353

print(sum(DP[N-1])%998244353)
