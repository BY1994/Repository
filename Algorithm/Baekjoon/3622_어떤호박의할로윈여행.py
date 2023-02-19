"""
3622 어떤 호박의 할로윈 여행

문제에 테두리가 만나는 부분은 어떻게 처리하라는 안내가 없다.
=> 테두리가 만나는 것도 문제 없는 상황

조건이 많으니 반례 많이 만들 수 있을 것

질문 답변 남기기
https://www.acmicpc.net/board/view/9731
두 고리가 반드시 큰 고리 안에 작은 고리 관계로 된다고 가정한 코드여서
A+B <= P 를 고려해야한다고 답변함
"""

A, a, B, b, P = map(int, input().split())
possible = 0
if A + B <= P:
    possible = 1
elif a >= B and A <= P:
    possible = 1
elif b >= A and B <= P:
    possible = 1

if possible:
    print("Yes")
else:
    print("No")
