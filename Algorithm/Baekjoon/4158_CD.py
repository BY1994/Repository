"""
4158 CD

투포인터 혹은 이분탐색

10억이기 때문에 count 를 사용할 수 없음

0, 0 이 나올 때까지 여러번 입력 받는 거 안 해서 틀림
https://www.acmicpc.net/board/view/90062
"""
import sys
input = sys.stdin.readline

while True:    
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    A = []
    B = []
    for i in range(N):
        A.append(int(input()))
    for i in range(M):
        B.append(int(input()))

    ans = 0
    p1, p2 = 0, 0
    while p1 < N and p2 < M:
        if A[p1] == B[p2]:
            ans += 1
            p2 += 1
            p1 += 1
        elif A[p1] > B[p2]:
            p2 += 1
        else:
            p1 += 1
    print(ans)
