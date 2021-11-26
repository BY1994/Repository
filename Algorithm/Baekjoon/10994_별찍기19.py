"""

4
바깥 별 13개
별 2개 + 스페이스 11개
*           * 안쪽 스페이스 9개
3
바깥 별 2개 + 스페이스 2개 + 별 9개
* ********* *
* *       * * 안쪽 스페이스 5개 (왼쪽 오른쪽 스페이스는 안 셌음)
2
* * ***** * *
바깥 별 2개 + 스페이스 2개 + 별 5개
1
바깥별 3개 * 2 쌍 + 중앙 별 1개
* * * * * * *

"""
def start(cur, n):
    if cur <= 1:
        print('* '*(n-1), end="")
        print('*', end="")
        print(' *'*(n-1))
    else:
        print('* '*(n - cur), end="")
        print('*'*((cur-1)*4 + 1), end="")
        print(' *'*(n - cur))
        
        print('* '*(n - cur+1), end="")
        print(' '*((cur-2)*4 + 1), end="")
        print(' *'*(n - cur + 1))

        start(cur-1, n)

        print('* '*(n - cur + 1), end="")
        print(' '*((cur-2)*4 + 1), end="")
        print(' *'*(n - cur + 1))

        print('* '*(n - cur), end="")
        print('*'*((cur-1)*4 + 1), end="")
        print(' *'*(n - cur))

N = int(input())
start(N, N)
