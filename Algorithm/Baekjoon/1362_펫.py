"""
1362 펫

시뮬레이션
"""

TC = 1
while True:
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break

    flag = 0
    while True:
        command, value = input().split()
        value = int(value)
        if command == '#' and value == 0:
            break
        if command == 'E':
            w -= value
        else:
            w += value
        if w <= 0:
            flag = 1
    if flag == 1:
        print(TC, "RIP")
    elif o < w*2 and w < o*2:
        print(TC, ":-)")
    else:
        print(TC, ":-(")
    TC += 1

# 숏코딩 참고
# https://www.acmicpc.net/source/18483400
"""
I,c=lambda:input().split(),1
while 1:
 p,w=map(int,I())
 if not(p|w):break
 o,n=I();d=0
 while o!='#':w+=int(n)*[1,-1][o=='E'];d|=w<1;o,n=I()
 print(c,[f':-{"()"[p/2<w<p*2]}','RIP'][d]);c+=1
"""
