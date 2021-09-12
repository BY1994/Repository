"""
2021 Hacker Cup

A2 Weak Typing

output 이 잘리지 않게 idle shell 말고
cmd 창에서 실행하기

input 길이가 80만이라서 N^2으로 풀면 초 단위를 넘어가게 된다...
A1과 다른 솔루션이 필요

mod 하는 걸 빼먹어서 Wrong Answer 나왔었음...

아이디어
FXXFXFOOXF
0000001122 누적합 6
각 시작 점에서부터 윈도우를 늘려간다고 생각하면
0 + 0 + ...+ 1 +1 + 2 + 2 = 6
나오고 시작점을 O라고 생각하면 0 + 0 + 1 + 1 = 2 가 나온다.
(베이스를 누적합에서 빼주면 된다)
F 만 잘 처리해주면
6 * 5개 + 2 * 3개 = 36이 나온다.
F 처리는, 시작점 처리는 누적해서 X나 O 만나면 한 번에 더하도록 했다.
"""


import sys
#sys.stdin = open("weak_typing_chapter_2_input.txt")
#sys.stdout = open("21_R1_02_weak_typing_chapter_2_final_output.txt", "wt")


T = int(input())

for tc in range(1, T+1):
    ans = 0
    n = int(input())
    w = input()

    array = [0] * n
    letter = -1

    # 총합 알아두기
    total = 0
    for i in range(n):
        if w[i] == 'F':
            if i > 0:
                array[i] = array[i-1]    
        elif letter == -1: letter = ord(w[i])
        elif letter != ord(w[i]):
            array[i] = array[i-1] + 1
            letter = ord(w[i])
        else:
            array[i] = array[i-1]
        total += array[i]

    # 누적합 이용해서 답 구하기
    cum = 1
    for i in range(n):
        if w[i] == 'F':
            cum += 1
        else:
            ans = (ans + (total - array[i]*(n-i) ) * cum) % 1000000007
            cum = 1
        total -= array[i] # 이미 지나간 거가 총합에 더해져있으면 나중에 뺄 수가 없음
        
    print(f"Case #{tc}: {ans}")
