"""
1652 누울 자리를 찾아라

문제 설명 추가 (X 로 끊기면 다시 자리 있는지 찾아야함)
https://www.acmicpc.net/board/view/9994

2칸 연속 칸 세기이므로 난이도를 (현재 브론즈 I) 더 낮춰도 될 것으로 보임
기본 2차원 배열 탐색
"""

N = int(input())
room = []
for i in range(N):
    room.append(input())

hori, verti = 0, 0
for i in range(N):
    cur = 0
    for j in range(N):
        if room[i][j] == 'X':
            if cur >= 2:
                hori += 1
            cur = 0
        else:
            cur += 1
    if cur >= 2:
        hori += 1

for j in range(N):
    cur = 0
    for i in range(N):
        if room[i][j] == 'X':
            if cur >= 2:
                verti += 1
            cur = 0
        else:
            cur += 1
    if cur >= 2:
        verti += 1

print(hori, verti)
            
