"""
11434 Ampelmännchen

그리디 알고리즘보다
단순 대소비교에 가깝지 않나

help(int) 이런 식으로 쓰면 docstring 을 보여준다고 한다.
내부적으로 strip 을 해서 \n 등의 문자를 제거해준다는 설명
"""

for K in range(int(input())):
    happy = 0
    n, W, E = map(int, input().split())
    for i in range(n):
        Lww, Lwe, Lew, Lee = map(int, input().split())
        happy += max(Lww*W + Lew*E, Lwe*W + Lee*E)
    print("Data Set {}:".format(K+1))
    print(happy)
    print()
