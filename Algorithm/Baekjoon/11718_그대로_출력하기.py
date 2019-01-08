# 백준 알고리즘 11718
# 백준 Online Judge - 문제 - 단계별로 풀어보기 - 입/출력 받아보기 - 그대로 출력하기
# 최초 풀이 2019.01.03 PBY
# 최종 답안 2019.01.08 PBY

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