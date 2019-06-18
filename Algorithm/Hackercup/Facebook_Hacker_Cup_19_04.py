"""
facebook Hacker Cup 2019 Qualification Round 
Trees as a Service

Input)
6
3 1
1 2 3
3 3
1 2 2
2 3 3
3 1 1
4 2
2 1 2
1 4 3
6 3
2 4 3
6 5 4
1 2 6
7 4
7 3 5
4 1 2
6 3 6
6 4 5
12 9
1 5 7
11 2 6
9 4 12
8 12 6
10 1 7
4 3 12
3 10 6
8 11 8
2 5 10

2019.06.15 PBY 최초 작성
"""

# input
T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    ans = "Impossible"
    origin = [-1] * N
    nodes_set = []
    remain_set = []

    # 0 들어갈 자리 찾기
    for nodes in range(M):
        x, y, z = map(int, input().split())
        if origin[x-1] == -1 and x != z:
            origin[x-1] = z
        if origin[y-1] == -1 and y != z:
            origin[y-1] = z
        nodes_set.append([x,y,z])

    for index in range(N):
        if origin[index] == -1:
            remain_set.append(index)

    # 1차 체크
    for check in range(len(remain_set)):
        test = origin[:]
        test[remain_set[check]] = 0
        for x,y,z in nodes_set:
            flag = 0
            current = x-1
            while flag == 0:
                if x == z:
                    flag = 1
                    break
                
                if test[current] == -1:
                    test[current] = z
                    flag = 1
                    break
                elif test[current] == z:
                    flag = 1 # 성공시 flag = 1
                    break
                elif test[current] == 0:
                    break
                else:
                    if current == test[test[current]-1]-1:
                        flag = 1
                        break
                    current = test[current]-1
            if flag == 0:
                test[x-1] = z

            flag = 0
            current = y-1
            while flag == 0:
                if y == z:
                    flag = 1
                    break
                
                if test[current] == -1:
                    test[current] = z
                    flag = 1
                    break
                elif test[current] == z:
                    flag = 1
                    break
                elif test[current] == 0:
                    break
                else:
                    if current == test[test[current]-1]-1:
                        flag = 1
                        break
                    current = test[current] - 1
            if flag == 0:
                test[y-1] = z

        # 2차 체크
        for x,y,z in nodes_set:
            flag = 0
            current = x-1
            while flag == 0:
                if x == z:
                    flag = 1
                    break
                
                if test[current] == z:
                    flag = 1
                    break
                elif test[current] == 0:
                    break

                if test[current] == -1:
                    test[current] = z

                if current == test[test[current]-1]-1:
                    break
                current = test[current]-1
            if flag == 0:
                break

            flag = 0
            current = y-1
            while flag == 0:
                if y == z:
                    flag = 1
                    break
                
                if test[current] == z:
                    flag = 1
                    break
                elif test[current] == 0:
                    break

                if test[current] == -1:
                    test[current] = z

                if current == test[test[current]-1]-1:
                    break
                current = test[current]-1
            if flag == 0:
                break
        else:
            # break를 안 했으면 ans인 것
            ans = ' '.join(map(str,test))
            
        if ans != "Impossible":
            break
    
        
    print("Case #%d: %s" %(case+1, ans))


"""
1. 가능한 것 채우고, 0 들어갈 곳들 정함
(없으면 Impossible을 출력하면 되고, 하나인 경우 바로 체크하면 됨)

2. 하나씩 체크하면서 부모 노드로 쭉 올라갔을 때 0을 만나면 내 자리에 숫자를 넣고,
아직 부모 노드에 자리가 비어있으면 채워넣기

3. 처음부터 다시 체크하면서 잘못된 거 있는지 확인
잘못되면 바로 다른 경우의 수로 이동하고, 하나라도 가능하면 즉시 종료!

"""
