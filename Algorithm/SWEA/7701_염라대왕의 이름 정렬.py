"""
7701 염라대왕

2019.07.08 PBY 최초작성
"""

# 문제 오류: input 받을 때 '\r'이 그대로 들어옴.....ㅠㅠ
# 내 실수: 중간에 range(100) 을 range(N)이라고 잘못 써서 틀린 케이스가 생겼다.

T = int(input())
for testcase in range(T):
    N = int(input())
    print("#%d" %(testcase+1))
    namebook = [[0] for _ in range(100)]
    for _ in range(N):
        temp = input().strip()
        print(temp, len(temp))
        namebook[len(temp)-1][0] += 1
        namebook[len(temp)-1].append(temp)
    for i in range(100):
        if namebook[i][0] > 0:
            temp_list = list(set(namebook[i][1:]))
            temp_list.sort()
            namebook[i][1:] = temp_list
            namebook[i][0] = len(temp_list)
    for i in range(100):
        for j in range(namebook[i][0]):
            print(namebook[i][j+1])

# 런타임 에러
"""
T = int(input())
for testcase in range(T):
    N = int(input())
    print("#%d" %(testcase+1))
    namebook = [[0] for _ in range(50)]
    for _ in range(N):
        temp = input()
        namebook[len(temp)-1][0] += 1
        namebook[len(temp)-1].append(temp)
    for i in range(N):
        if namebook[i][0] > 0:
            temp_list = list(set(namebook[i][1:]))
            temp_list.sort()
            namebook[i][0] = len(temp_list)
            namebook[i][1:] = temp_list[:]
    for i in range(len(namebook)):
        for j in range(namebook[i][0]):
            print(namebook[i][j+1])
"""


# 작은 수가 먼저 와야한다는 걸 고려 안함
"""
T = int(input())
for testcase in range(T):
    N = int(input())
    print("#%d" %(testcase+1))
    namebook = []
    for _ in range(N):
        namebook.append(input())
    namebook = list(set(namebook))
    namebook.sort()
    for i in range(len(namebook)):
        print(namebook[i])
"""    
