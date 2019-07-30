"""
7465 창용 마을 무리의 개수

input)
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

2019.07.08 PBY 최초 작성
2019.07.30 PBY 다시 작성
"""     

def union_group(ind, N, town):
    for j in range(N):
        if town[ind][j] == 1:
            group[group[0]].extend([i, j])
            town[ind][j] = 0
            town[j][ind] = 0
            union_group(j, N, town)

for testcase in range(int(input())):
    
    # input
    N, M = map(int, input().split())
    town = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        town[a-1][b-1] = 1
        town[b-1][a-1] = 1

    # 개인 그룹
    ans = 0
    for i in range(N):
        if sum(town[i][:]) == 0:
            ans += 1
            
    # find group
    group = [0]
    for i in range(N):
        flag = 0
        for j in range(N):
            if town[i][j] == 1:
                flag += 1
                if flag == 1: # 첫번째 아는 사람이면
                    group[0] += 1
                    group.append([i, j])
                    town[i][j] = 0
                    town[j][i] = 0
                else: # 다른 아는 사람이면
                    group[group[0]].extend([i, j])
                    town[i][j] = 0
                    town[j][i] = 0
                union_group(j, N, town)                    
            
    
    print("#%d %d" %(testcase+1, ans + group[0]))

# 반만 맞음
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
"""
