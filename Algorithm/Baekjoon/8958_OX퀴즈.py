""" 
백준 알고리즘 8958
백준 Online Judge - 문제 - 단계별로 풀어보기 - 1차원 배열 사용하기 - OX퀴즈

문제)
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
OOXXOXXOOO

입력)
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
10

출력)
각 테스트 케이스마다 점수를 출력한다.

최초 작성 2019.01.28 PBY
"""

testcase = int(input())
for tc in range(testcase):
    scores = input()
    onum = ans = 0

    for score in scores:
        if score == 'O':
            onum += 1
        else:
            onum = 0
        ans += onum

    print(ans)

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5