""" 
백준 알고리즘 1157
백준 Online Judge - 문제 - 단계별로 풀어보기 - 문자열 사용하기 - 단어 공부

문제)
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력)
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
Mississipi

출력)
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
?

최초 작성 2019.02.07 PBY
"""
s = input().upper()

sset = list(set(s))
slist = [0]*len(sset)

for i in range(len(sset)):
    slist[i] =s.count(sset[i])

sorted_slist = sorted(slist)

if len(s) > 1:
    if sorted_slist[-1] == sorted_slist[-2]:
        print('?')
    else:
        print(sset[slist.index(sorted_slist[-1])])
else:
    print(s)

# 런타임 에러 발생 - 글자수가 하나만 들어오는 경우 에러 발생
# if 문으로 에러를 해결하였다.


# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5