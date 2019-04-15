"""
문제 예제
21 70 80
26 65 80
0 0 0

반례 찾으려고 만든 예제
24 1 24
0 0 0

"""
while True:
    M, A, B = map(int, input().split())
    if M == 0 and A == 0 and B == 0:
        break
    totaltime = round(abs(M/A-M/B)*60*60)

    s = totaltime % 60
    m = ((totaltime - s)//60) % 60
    h = (totaltime - s - m*60) // 3600

    print(h, end=":")
    print("%02d" %m, end=":")
    print("%02d" %s)


# 실패한 코드
# 반올림을 마지막만 해주면 안 된다.
"""
while True:
    M, A, B = map(int, input().split())
    if M == 0 and A == 0 and B == 0:
        break
    print(int(abs(M/A-M/B)), end=":")
    print("%02d" %(int(abs(M/A-M/B)*60 - int(abs(M/A-M/B)))), end=":")
    print("%02d" %(round((abs(M/A-M/B)*60-int(abs(M/A-M/B)*60))*60)))
"""
