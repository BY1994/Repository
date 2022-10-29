"""
1598 꼬리를 무는 숫자 나열

수학
4의 배수 주의해야함!!

반례
4 5
정답 4 틀린답 1 / 3

반례
https://www.acmicpc.net/board/view/88348
20 39
정답 6 틀린답 5
"""

A, B = map(int, input().split())
print(abs((A-1) // 4 - (B-1) // 4) + abs((A-1) % 4 - (B-1) % 4))

# 틀렸습니다
"""
A, B = map(int, input().split())
print(abs(A // 4 - B // 4) + abs((A-1) % 4 - (B-1) % 4))
"""

# 틀렸습니다
"""
A, B = map(int, input().split())
print(abs(A // 4 - B // 4) + abs(A % 4 - B % 4))
"""
