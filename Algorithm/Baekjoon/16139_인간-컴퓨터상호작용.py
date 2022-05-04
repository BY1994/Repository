"""
16139 인간-컴퓨터 상호작용

누적합

파이썬으로 풀면 시간초과 때문에 50점이 나오는 듯하다.
sys.stdin.readline 이나 sys.stdout.write 사용하고도 50점이 나와서
pypy3 로 제출했더니 통과했다.

https://joey09.tistory.com/134
https://www.acmicpc.net/board/view/72802
"""

import sys
input = sys.stdin.readline

S = input()[:-1] # \n 때문에
lenS = len(S)
a = ord('a')

cursum = [[0 for i in range(26)] for j in range(lenS+1)]
for i in range(lenS):
    cursum[i+1][ord(S[i])-a] += 1
    for j in range(26):
        cursum[i+1][j] += cursum[i][j]

for q in range(int(input())):
    alpha, l, r = input().split()
    alpha = ord(alpha)-a
    l = int(l)
    r = int(r)
    sys.stdout.write(str(cursum[r+1][alpha]-cursum[l][alpha]) + '\n')
