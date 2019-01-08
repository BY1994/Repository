# 백준 알고리즘 11718
# 백준 Online Judge - 문제 - 단계별로 풀어보기 - 입/출력 받아보기 - 그대로 출력하기
# 최초 풀이 2019.01.03 PBY
# 최종 답안 2019.01.08 PBY

"""
# 입력
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

Hello
Baekjoon
Online Judge

# 출력
입력받은 그대로 출력한다.

Hello
Baekjoon
Online Judge
"""

# 답안 참고한 사이트 https://chuckolet.tistory.com/4

import sys
for i in sys.stdin:
    print(i, end="")


# 1. 실패한 코드 런타임 에러

# import sys
# for i in sys.stdin:
#    pirnt(i, end="")

# 2. 실패한 코드 런타임 에러

# while True:
#   print(input())


# 2번의 코드는 파이썬에서 동작이 느리기 때문이지만,
# 1번의 코드는 print에서 오타가 났기 때문인 것을 발견하고
# 수정하여 제출하였다.