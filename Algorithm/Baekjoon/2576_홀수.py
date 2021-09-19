"""
2576 홀수

합, 최소값 구하기 기초 문제
"""

ans = 101
total = 0
for i in range(7):
    num = int(input())
    if num % 2:
        ans = num if ans > num else ans
        total += num

if ans < 100:
    print(total)
    print(ans)
else:
    print(-1)

"""
반례 찾기
https://www.acmicpc.net/board/view/66615

마지막에 홀수값이 들어온 경우 그거를 최소값으로 처리 못하는 코드
2
4
6
8
10
12
13
"""
