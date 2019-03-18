"""
10996 별찍기 21

2019-03-18 PBY 최초작성
"""

N = int(input())

if N == 1:
    print('*')
elif N % 2 == 0: # 짝수면
    for i in range(N*2):
        if i % 2 == 0:
            print('* '*(N//2 + N%2))
        else:
            print(' ' + '* '*(N//2 + N%2))

else:
    for i in range(N*2):
        if i % 2 == 0:
            print('* '*(N//2 + N%2))
        else:
            print(' ' + '* '*(N//2))
