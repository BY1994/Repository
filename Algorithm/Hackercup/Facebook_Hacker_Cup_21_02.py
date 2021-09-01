"""
2021 Facebook Hacker Cup
Problem A2

cmd 창에서 실행하면 file 이 잘 생성되는데,
idle에서 실행하면 마지막 줄이 짤린다....
"""

import sys
#sys.stdin = open("21_02_final_input_consistency2.txt")
sys.stdout = open("21_02_output.txt", "wt")

T = int(input())
norm = ord('A')

for tc in range(T):
    # 초기화 (Floyd 위한 배열 준비)
    ans = 10000000 # INF
    s = input()
    # array = [[10000000]*26]*26 # 이렇게 하면 얕은 복사
    array = [[10000000]*26 for _ in range(26)]

    for i in range(26):
        array[i][i] = 0
        
    edge = int(input())
    for e in range(edge):
        line = input()
        array[ord(line[0]) - norm][ord(line[1]) - norm] = 1

    # Floyd Warshall
    for k in range(26): # 거쳐가는 노드
        for i in range(26): # 출발 노드
            for j in range(26): # 도착 노드
                if array[i][k] + array[k][j] < array[i][j]:
                    array[i][j] = array[i][k] + array[k][j]

    # 모든 도착지마다 최적의 경로 찾기
    for i in range(26):
        temp = 0
        for j in s:
            temp += array[ord(j) - norm][i]
        ans = temp if temp < ans else ans

    if ans == 10000000:
        ans = -1
    print(f"Case #{tc+1}: {ans}")
