"""
백준
1712 손익분기점

A 고정 비용
B 가변 비용 (노트북 1대당 비용)
C 판매비용 (노트북 1대당 판매값)

제출 전에 질문 검색 게시판을 봤는데,
https://www.acmicpc.net/board/view/73204
내가 Zero division error를 처리 안 한 것을 발견하였다.
(1) if문 혹은 (2) try except ZeroDivisionError 가 있다.

+ 이 문제에서 21억 자연수 범위를 설정한 이유는,
N까지 for문 돌리는 사람들이 시간초과나게 하기 위해서

+ 대부분의 사람들이 통과하지 못한 반례는 이것이었다.
100 10 100
정답: 2
대부분의 오답: 1

대부분 손익분기점의 경우 +1을 해줘야하는 부분에서 실수가 있었다.
"""

A, B, C = map(int, input().split())
if B - C >= 0: print(-1)
else: print(A // (C - B) + 1)

"""
# 초기버전 코드
A, B, C = map(int, input().split())
N = A // (C - B)
print(N+1 if N > 0 else -1)
"""
