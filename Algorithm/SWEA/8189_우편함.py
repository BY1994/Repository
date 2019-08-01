"""
8189 우편함

★충격적인 사실★
python에서 round(1.5)는 2지만, round(0.5)는 0이다!!!!!!!!!!!!!!!!!!!!!

input)
2
4 100 10
1 2 3 4
8 4 50
1 2 3 4 50 90 91 100

2019.08.01 PBY 최초작성
"""
# 40 문제 중 22 문제 정
for testcase in range(int(input())):

    print("#%d " %(testcase+1), end="")
    
    N, A, B = map(int, input().split())
    letters = list(map(int, input().split()))
    timeTable = [0]*1001
    for l in letters:
        timeTable[l] = 1

    # 최대 시간이 1000 시간이므로 for문으로 일일히 확인
    ansCheck = 0
    numLetter = 0
    latest = letters[0]
    
    for time in range(1001):

        if ansCheck == N:
            break

        # 편지 배달
        if timeTable[time] == 1:
            numLetter += 1

        # 우편함 비우는 시점
        if numLetter == A or latest == time-B:

            print((str(time)+" ")*(int(numLetter/2)+numLetter%2), end="")

            letters = letters[round(numLetter/2):]
            ansCheck += round(numLetter/2)
            numLetter = numLetter - round(numLetter/2)
            if len(letters) == 0: break
            latest = letters[0]

    print()
