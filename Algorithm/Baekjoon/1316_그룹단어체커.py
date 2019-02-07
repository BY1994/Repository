""" 
백준 알고리즘 1316
백준 Online Judge - 문제 - 단계별로 풀어보기 - 문자열 사용하기 - 그룹 단어 체커

문제)
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력)
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
4
aba
abab
abcabc
a

출력)
첫째 줄에 그룹 단어의 개수를 출력한다.
1

최초 작성 2019.02.07 PBY
"""
testcase = input()
count = 0

for tc in range(int(testcase)):
    s = input()
    slist = []
    if len(s) == 1:
        count += 1
    else:
        slist += s[0]
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                if s[i+1] not in slist:
                    slist += s[i+1]
                else:
                    break
        else:
            count += 1
print(count)


# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5