"""
2109 순회강연

반례 궁금함!!!

문제 입력
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
출력 185

인덱스 에러는 0 입력을 처리 안 함

3
1 1
10 2
10 2
내 답 11
정답 20

내가 만든 반례
3
70 3
60 3
50 3
내 답 70
정답 180

4
70 3
60 3
50 3
40 3
오답 220
정답 180

4
20 2
30 2
40 3
40 3
오답 80
정답 110
"""
visited = [0]*10001

N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: -x[0])
    for i in range(N):
        for j in range(pos[i][1], 0, -1): # 1 일차까지만
            if visited[j] == 0:
                ans += pos[i][0]
                visited[j] = 1
                break

print(ans)

# 반례 못 찾음
"""
N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: (-x[1], -x[0]))
    mtemp = 0
    date = pos[0][1]
    while(date):
        for i in range(mtemp, N):
            if pos[i][1] < date:
                break
            else:
                if pos[mtemp][0] < pos[i][0]:
                    mtemp = i

        ans += pos[mtemp][0]
        if mtemp == N-1:
            break
        mtemp += 1
        date = min(date-1, pos[mtemp][1])

print(ans)
"""

# 반례 못 찾음
"""
N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: (-x[1], -x[0]))
    mtemp = 0
    cur = pos[0][1]
    i = 0
    while(i < N and cur > 0):
#        print("###i ", i)
#        print(pos)
        if pos[i][1] < cur:
#            print("###", mtemp)
            ans += pos[mtemp][0]
            cur = pos[i][1]
            mtemp += 1
            i = mtemp
        else:
#            pos[i][1] -= 1
            if pos[mtemp][0] < pos[i][0]:
                mtemp = i
            if i == N-1:
                ans += pos[mtemp][0]
                cur -= 1
                if pos[i][1] > cur:
                    i = mtemp
                    mtemp += 1
            i += 1


print(ans)
"""

# 반례
# https://www.acmicpc.net/board/view/68574
"""
N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: (-x[1], -x[0]))
    mtemp = 0
    cur = pos[0][1]
    i = 0
    while(i < N):
#        print("###i ", i)
#        print(pos)
        if pos[i][1] < cur:
#            print("###", mtemp)
            ans += pos[mtemp][0]
            cur = pos[i][1]
            mtemp += 1
            i = mtemp
        else:
            pos[i][1] -= 1
            if pos[mtemp][0] < pos[i][0]:
                mtemp = i
            if i == N-1:
                ans += pos[mtemp][0]
#                cur -= 1
                if pos[i][1] > 1:
                    i = mtemp
                    mtemp += 1
            i += 1


print(ans)
"""


# cur 값을 하루씩 적게 만들면서 돌아야하는데, 그게 적용 안 됨...
"""
N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: (-x[1], -x[0]))
    mtemp = 0
    cur = pos[0][1]
    i = 0
    while(i < N):
#        print("###i ", i)
        if pos[i][1] < cur:
#            print("###", mtemp)
            ans += pos[mtemp][0]
            cur = pos[i][1]
            mtemp += 1
            i = mtemp
        else:
            if pos[mtemp][0] < pos[i][0]:
                mtemp = i
            i += 1

    ans += pos[mtemp][0]
print(ans)
"""

# 반례
# https://www.acmicpc.net/board/view/1885

"""
N = int(input())
pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

ans = 0

if len(pos):
    pos.sort(key = lambda x: (x[1], -x[0]))
    mtemp = 0
    cur = pos[0][1]
    for i in range(N):
        if pos[i][1] > cur:
            ans += pos[mtemp][0]
            cur = pos[i][1]
            mtemp = i
        else:
            if pos[mtemp][0] < pos[i][0]:
                mtemp = i

    ans += pos[mtemp][0]
print(ans)
"""
