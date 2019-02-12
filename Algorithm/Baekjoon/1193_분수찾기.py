""" 
백준 알고리즘 1193
백준 Online Judge - 문제 - 단계별로 풀어보기 - 규칙 찾기 - 분수찾기

문제)
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
14

출력)
첫째 줄에 분수를 출력한다.
2/4

최초 작성 2019.02.11 PBY
최종 제출 2019.02.11
"""

# input
cnt = int(input())
state = 1 # 1이면 앞에서 뒤로 숫자 옮기기, 2면 뒤에서 앞으로 숫자 옮기기
up = 1 # 시작 지점
down = 1

# 규칙대로 숫자 변화
for i in range(1, cnt):
    if state == 1 and up != 1: # 앞에서 뒤로 숫자를 옮기다가
        up -= 1
        down += 1
    elif state == 1 and up == 1: # 더 이상 옮길 수 없으면 방향 전환
        down += 1
        state = 2
    elif state == 2 and down != 1: # 뒤에서 앞으로 숫자를 옮기다가
        up += 1
        down -= 1
    elif state == 2 and down == 1: # 더 이상 옮길 수 없으면 방향 전환
        up += 1
        state = 1

# output
print('{}/{}'.format(up, down))


# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5