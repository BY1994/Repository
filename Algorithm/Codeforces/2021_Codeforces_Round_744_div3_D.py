"""
Codeforces Round #744 (Div.3)

D

index 를 두 종류를 썼더니,
index 이름이 헷갈려서 시간을 많이 잡아먹었다.
변수명이 좀 길어져도 이해하기 쉬운 거로 하는 게 좋을 것 같다.

샘플 케이스는 맞았지만, wrong answer가 나왔다.
"""

# wrong answer
def print_ans(n, array):
    print(n)
    for j in range(n):
        print(*ans[j], sep = " ")
    

tc = int(input())
for _ in range(tc):
    n = int(input())
    people = list(map(int, input().split()))
    sorted_i = sorted(range(len(people)), key=lambda k: people[k], reverse = True)
    inda = 0
    indb = 1
    for i in range(n):
        if people[sorted_i[i]] != 0:
            inda = i # for sorted i index
            break

    for j in range(i+1, n):
        if people[sorted_i[j]] != 0:
            indb = j
            break

    ans = []
    ansn = 0

    while inda < n and indb < n:
        flag = 0

        bigi = sorted_i[inda] # people index
        nextbigi = sorted_i[indb]
        #print(bigi, inda)
        #print(nextbigi, indb)
        #print(people)
        people[bigi] -= 1
        people[nextbigi] -=1

        if people[bigi] < 0:
            break
        elif people[bigi] == 0:
            for j in range(inda+1, n):
                if people[sorted_i[j]] != 0 and j != indb:
                    inda = j
                    break
            else:
                flag += 1
                #break

        if people[nextbigi] < 0:
            break
        elif people[nextbigi] == 0:
            for j in range(indb+1, n):
                if people[sorted_i[j]] != 0 and j != inda:
                    indb = j
                    break
            else:
                flag += 1
                #break
            
        ansn += 1
        ans.append([bigi+1, nextbigi+1])

        # if next is not possible
        if flag >= 1:
            break

    print_ans(ansn, ans)

# time limit
"""
def print_ans(n, array):
    print(n)
    for j in range(n):
        print(*ans[j], sep = " ")
    

tc = int(input())
for _ in range(tc):
    n = int(input())
    people = list(map(int, input().split()))
    ans = []
    ansn = 0

    while True:
        big = max(people)
        bigi = people.index(big)
        people[bigi] = 0
        if big == 0:
            print_ans(ansn, ans)
            break

        nextbig = max(people)
        nextbigi = people.index(nextbig)
        people[bigi] = big # recover

        if nextbig == 0:
            print_ans(ansn, ans)
            break

        people[bigi] -= 1
        people[nextbigi] -=1
        ansn += 1
        ans.append([bigi+1, nextbigi+1])
"""
