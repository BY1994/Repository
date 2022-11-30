"""
2145 숫자 놀이

구현
각 자리수를 더해서 한 자리가 될 때까지 반복
"""

while True:
    N = int(input())
    if N == 0:
        break
    while N // 10:
        temp = 0
        while N:
            temp += N % 10
            N //= 10
        N = temp
    print(N)
