"""
2231 분해합


# https://www.acmicpc.net/board/view/78395
문제에서 제시된 범위 내에서 분해합과 원래 수의 차이의 최댓값은 53입니다. ex)900052
41로만 해도 맞는 것은 데이터가 부족하기 때문입니다.


# 반례
https://www.acmicpc.net/board/view/77583
17 넣으니까 13 나와야하는데 -1이 나옴;;;
(max(0,N-55)) 처리해주고나서 해결...
"""

N = input()
l = len(N)
N = int(N)

ans = 0
for i in range(max(0,N-55), N+1):
    temp = i
    cur = i
    for j in range(l):
        temp += cur % 10
        cur //= 10
    if temp == N:
        ans = i
        break

print(ans)
