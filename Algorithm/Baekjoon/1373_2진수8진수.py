"""
1373 2진수 8진수

12/2 틀렸습니다
=> 반례 처리가 빠짐
0일 때 처리를 해야함
https://www.acmicpc.net/board/view/103822

0 일 때 예외처리를 추가하고
12/10 맞았습니다
"""
number = input()
N = len(number)
if N == 1 and int(number[0]) == 0:
    print(0)
else:
    ind = 0
    temp = 0
    while ind < N % 3:
        temp <<= 1
        temp += int(number[ind])
        ind += 1
    if temp:
        print(temp, end='')

    while ind < N:
        temp = ((int(number[ind]))<<2) + ((int(number[ind+1]))<<1) +\
                int(number[ind+2])
        ind += 3
        print(temp, end='')
    print()
