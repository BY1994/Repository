"""
2021 Facebook Hackercup

A1 Weak Typing 1

output 이 잘리지 않게 idle shell 말고
cmd 창에서 실행하기
"""

import sys
#sys.stdin = open("weak_typing_chapter_1_input.txt")
#sys.stdout = open("21_R1_01_weak_typing_chapter_1_final_output.txt", "wt")


pos = ['O', 'X'] # left poss = F, X / right poss = F, O
T = int(input())

for tc in range(1, T+1):
    ans = 0
    n = input() # do not use
    w = input()

    hand1 = 0 # start from left hand
    hand2 = 1 # start from right hand
    a = 0 # hand 1 count
    b = 0 # hand 2 count
    for letter in w:
        if letter == 'F': continue
        if letter != pos[hand1]:
            hand1 = (hand1 + 1) % 2
            a += 1
        if letter != pos[hand2]:
            hand2 = (hand2 + 1) % 2
            b += 1
            
    ans = a if a < b else b
    print(f"Case #{tc}: {ans}")
