"""
11653 소인수분해

에라토스테네스의 체 사용시 시간 초과
"""

N = int(input())

i = 2
while i < N+1:
    if N % i == 0:
        print(i)
        N //= i
        i -= 1
    i += 1
