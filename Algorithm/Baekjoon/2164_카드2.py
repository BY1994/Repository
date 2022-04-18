"""
2164 카드2

실수한 포인트
re 에 N-1 을 안 넣고 500000 을 넣어서 잘못된 답 나옴
"""

N = int(input())
Q = list(range(1, 1000001))
fr = 0
re = N-1
count = 0
while fr < re:
    #print(fr, re, Q[:10])
    if count % 2 == 0:
        fr += 1
    else:
        re += 1
        Q[re] = Q[fr]
        fr += 1
    count += 1

print(Q[fr])
