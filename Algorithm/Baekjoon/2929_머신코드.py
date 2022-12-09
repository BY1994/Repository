"""
2929 머신 코드

마지막 명령어는 NOP 개수를 고려하지 않아도 됨
python 중 실행시간이 1등이 나왔는데,
python 3.11 버전부터 실행시간이 개선되어서 최근 풀이가 빠르게 나오는 것이 아닐까 싶다.

portableangel 님의 8년 전 질문도 있었다.

https://www.acmicpc.net/board/view/75661
반례찾기
ZzzzzZ 를 하면 +3 이 필요해서 답으로 3이 출력되어야하는데,
위의 코드는 -1 이 출력되었다.
"""

code = input()
ans = 0
cur = 0
for i in range(len(code)):
    if ord(code[i]) >= ord('a'):
        cur += 1
    else:
        if cur % 4 > 0:
            ans += 4 - (cur % 4)
        cur = 1
print(ans)
