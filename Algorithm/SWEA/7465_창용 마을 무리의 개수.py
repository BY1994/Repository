"""
7465 창용 마을 무리의 개수

2019.07.08 PBY 최초작성
"""

for testcase in range(int(input())):
    ans = 0
    N, M = map(int, input().split())
    city = [N+1]*N
    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            if city[a-1] > b:
                city[a-1] = b
            if city[b-1] > b:
                city[b-1] = b
        else:
            if city[b-1] > a:
                city[b-1] = a
            if city[a-1] > a:
                city[a-1] = a

    for i in range(N):
        if city[i] < i+1:
            index = i
            saved = city[i]
            while True:
                if city[city[index]-1] < city[index]:
                    saved = city[city[index]-1]
                    index = city[index]-1
                else:
                    city[i] = saved
                    break

    ans += city.count(N+1)
    if ans == 0:
        ans = len(set(city))
    else:
        ans += len(set(city))-1

    print("#%d %d" %(testcase+1, ans))
