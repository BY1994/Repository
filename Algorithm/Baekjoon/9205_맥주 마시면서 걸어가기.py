"""
9205 맥주 마시면서 걸어가기

1. 틀렸습니다 => 질문검색 게시판을 보니 편의점이 항상 가까운 순서로 제시되는게 아니라고 한다.
2. 시간 초과 피하려고 possible이 1이 되면 더이상 돌지 말라고 해도 시간 초과가 떴다....
3. 메모리 초과 used를 큐로 넘기니까 메모리 초과가 났다.
4. 락 페스티벌까지 가까운 지점들을 큐로 순회하면서 가면 된다. 갔던 길은 다시 돌아올 필요가 없다.

입력)
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000

출력)
happy
sad


입력)
1
1
1000 0
0 1000
0 1001

출력)
sad

입력)
3
0
1000 1000
1000 1001
1
0 0
1000 0
0 2000
2
0 0
10000 0
0 1000
0 2000

출력)
happy
sad
happy

2019.04.09 최초 제출

"""

# 제출 성공

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    home = list(map(int, input().split()))
    conv = []
    for _ in range(N):
        conv.append(list(map(int, input().split())))
    fest = list(map(int, input().split()))

    possible = 0
    used = [False] * N
    q = deque([[home[0], home[1]]])
    lenq = len(q)
    while q:
        for i in range(lenq):
            x, y = q.popleft()
            if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
                possible = 1
                q = []
                break
            for j in range(N):
                if used[j] == True:
                    continue
                else:
                    if abs(x-conv[j][0]) + abs(y-conv[j][1]) <= 1000:
                        used[j] = True
                        q.append([conv[j][0], conv[j][1]])

    if possible == 0:
        print("sad")
    else:
        print("happy")

        
# 메모리 초과

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    home = list(map(int, input().split()))
    conv = []
    for _ in range(N):
        conv.append(list(map(int, input().split())))
    fest = list(map(int, input().split()))

    possible = 0
    used = [False] * N
    q = deque([[home[0], home[1], used[:]]])
    lenq = len(q)
    while q:
        for i in range(lenq):
            x, y, used = q.popleft()
            if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
                possible = 1
                q = []
                break
            for j in range(N):
                if used[j] == True:
                    continue
                else:
                    if abs(x-conv[j][0]) + abs(y-conv[j][1]) <= 1000:
                        used[j] = True
                        q.append([conv[j][0], conv[j][1], used[:]])

    if possible == 0:
        print("sad")
    else:
        print("happy")

        
# 시간초과
"""
def goFestival(x, y):
    global N, possible
    if possible == 1: # 시간 초과 피하기용!
        return
    if abs(x-fest[0]) + abs(y-fest[1]) <= 1000: # 언제든 락 페스티벌에 도착 가능하면
        possible = 1
        return

    for i in range(N):
        if used[i] == True:
            continue
        else:
            # 여기서 바로 락페스티벌에 갈 수 있으면 끝난다.
            if abs(x-conv[i][0]) + abs(y-conv[i][1]) <= 1000:# 여기서 갈 수 있는 거리여야 간다.
                used[i] = True
                goFestival(conv[i][0], conv[i][1])
                used[i] = False

                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    home = list(map(int, input().split()))
    conv = []
    for _ in range(N):
        conv.append(list(map(int, input().split())))
    fest = list(map(int, input().split()))

    possible = 0
    used = [False] * N
    goFestival(home[0], home[1])

    if possible == 0:
        print("sad")
    else:
        print("happy")
"""


# 틀렸습니다        
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    loca = []
    for _ in range(N+2):
        loca.append(list(map(int, input().split())))

    for i in range(N+1):
        if abs(loca[i][0] - loca[i+1][0]) + abs(loca[i][1]-loca[i+1][1]) > 1000:
            print("sad")
            break
    else:
        print("happy")
"""
