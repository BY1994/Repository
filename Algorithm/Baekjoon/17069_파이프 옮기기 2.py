"""
17069 파이프 옮기기 2

2019.07.05 PBY 최초작성
"""

# DP 연습문제

# 대각선은 4칸을 필요로 한다는 걸 생각 못해서 다음의 반례 등장
"""
5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""

# input
N = int(input())
house = []
for _ in range(N):
    house.append(input().split())

# 메모이제이션 [r][c][이전 칸에서 가로, 세로, 대각선으로 오는 경우의 수]
memo = [[[0]*3 for _ in range(N)] for __ in range(N)]
memo[0][1][0] = 1 # 가로 방향으로 오는 경우의 수 1개

# DP (위쪽부터 + 왼쪽부터)
for r in range(N):
    for c in range(N):
        # 가로로 오는 경우의 수
        if 0 < c and house[r][c-1] != "1":
            memo[r][c][0] += memo[r][c-1][0] + memo[r][c-1][2] # 이전 칸 가로 + 대각선
        # 세로로 오는 경우의 수
        if 0 < r and house[r-1][c] != "1":
            memo[r][c][1] += memo[r-1][c][1] + memo[r-1][c][2] # 이전 칸 세로 + 대각선
        # 대각선으로 오는 경우의 수
        if 0 < c and 0 < r and house[r-1][c-1] != "1" and house[r-1][c] != "1" and house[r][c-1] != "1":
            memo[r][c][2] += memo[r-1][c-1][0] + memo[r-1][c-1][1] + memo[r-1][c-1][2] # 이전 칸 가로 + 세로 + 대각선

# output
print(memo[r][c][0]+memo[r][c][1]+memo[r][c][2])
