"""
4493 가위 바위 보
"""

win = [[0 for i in range(256)] for j in range(256)]
_R, _P, _S = ord('R'), ord('P'), ord('S')
win[_R][_P] = 2
win[_P][_R] = 1
win[_R][_S] = 1
win[_S][_R] = 2
win[_P][_S] = 2
win[_S][_P] = 1
for tc in range(int(input())):
    n = int(input())
    score1, score2 = 0, 0
    for _ in range(n):
        p1, p2 = input().split()
        if win[ord(p1)][ord(p2)] == 1:
            score1 += 1
        elif win[ord(p1)][ord(p2)] == 2:
            score2 += 1
    if score1 > score2:
        print("Player 1")
    elif score1 < score2:
        print("Player 2")
    else:
        print("TIE")
