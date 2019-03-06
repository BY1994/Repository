""" 
백준 알고리즘 2477
참외밭

문제)
시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다. 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다. 어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다. 유레카! 1m^2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다.
1m^2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다. 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다. 다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.
예를 들어 참외밭이 위 그림과 같은 모양이라고 하자. 그림에서 오른쪽은 동쪽, 왼쪽은 서쪽, 아래쪽은 남쪽, 위쪽은 북쪽이다. 이 그림의 왼쪽위 꼭짓점에서 출발하여, 반시계방향으로 남쪽으로 30m, 동쪽으로 60m, 남쪽으로 20m, 동쪽으로 100m, 북쪽으로 50m, 서쪽으로 160m 이동하면 다시 출발점으로 되돌아가게 된다.
위 그림의 참외밭  면적은 6800m^2이다. 만약 1m^2의 넓이에 자라는 참외의 개수가 7이라면, 이 밭에서 자라는 참외의 개수는 47600으로 계산된다.
1m^2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

입력)
첫 번째 줄에 1m^2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1≤K≤20)가 주어진다. 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.

출력)
첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.

최초 작성 2019.03.06 PBY
"""
import sys
sys.stdin = open('2477_input.txt','r')

fruit = int(input())
# N, S, E, W = [], [], [], []

"""
2개를 이어붙였을 때, 
남동남동이 나오면 북서 - 동남
북서북서가 나오면 남동 - 서북
동북동북이 나오면 서남 - 북동
서남서남이 나오면 동북 - 남서

# 두 개 이어붙였을 때 그 다음에 나오는 거
북서남동남동
북서북서남동
서남동북동북
서남서남동북
"""
directions = ''
distances = [0] * 6
for i in range(6):
        direct, distance = input().split()
        directions += direct
        distances[i] = int(distance)

        # if direct == "4": # 북쪽으로 이동
        #         N.append(int(distance))
        # elif direct == "3": # 남쪽으로 이동
        #         S.append(int(distance))
        # elif direct == "2": # 서쪽으로 이동
        #         W.append(int(distance))
        # elif direct == "1": # 동쪽으로 이동
        #         E.append(int(distance))

directions = directions * 2 # 리스트 2개 이어붙이기
distances = distances * 2

for idx in range(len(directions)):
        if directions[idx:idx+2] == directions[idx+2:idx+4]:
                # 그 때의 idx+1부터 idx+3이 짧은 길이임
                # idx+4 부터 idx+5가 긴 길이임
                area = distances[idx+4]*distances[idx+5] - distances[idx+1]*distances[idx+2]
                break

print(area*fruit)

# # 가장 긴 두 넓이 찾기 => 반시계 방향 이동이라는 것 꼭 유념하기
# # 북으로 이동한게 남으로 이동한 것 보다 길면
# if N[0] > S[0]:
#         # 그리고 서로 이동한게 동으로 이동한 것 보다 길면 ㄱ 모양 밭
#         if W[0] > E[0]:
#                 # 전체 넓이 - 두번째 남 x 첫번째 동
#                 area = N[0]*W[0] - S[1]*E[0]
#         else: # 동으로 이동한 게 더 길면 ┘ 이런 모양 밭 (두번째 서쪽 x 첫번째 남쪽)
#                 area = N[0]*E[0] - W[1]*S[0]
# else: # 남으로 더 크게 이동했으면
#         # 서쪽으로 이동한 게 더 길면 ┌ 모양 밭 (첫번째 북쪽 x 두번째 동쪽)
#         if W[0] > E[0]:
#                 area = S[0]*W[0] - N[0]*S[1]
#         else: # 동쪽으로 이동한게 더 길면 └ 모양 밭 (두번째 북쪽 x 첫번째 서쪽)
#                 area = S[0]*E[0] - N[1]*S[0]
# print(area)

"""
다음으로 시도할 방법은 참외밭의 긴 부분에서 짧은 부분의 넓이를 빼는 것
"""

"""
아래 방법은 sample case는 맞는데...
다른 형태의 참외밭에는 문제가 생기는 듯?

fruit = int(input())
bat = [[0 for _ in range(1000)] for __ in range(1000)] # 밭의 최대가 500, 시작 지점이 어디여도 되도록 밭이 1/4이 되도록 했다.
start = [499, 499]
bat[start[0]][start[1]] = 1
area = 0
for _ in range(6): # input은 6번 들어옴
        direct, distance = input().split()
        if direct == "4": # 북쪽으로 이동
                for i in range(int(distance)):
                        start[0] -= 1 # 위로 이동
                        bat[start[0]][start[1]] = 1
                        #area -= 1 # 밑에서 두 번 갈 테니까 미리 빼줌
        elif direct == "3": # 남쪽으로 이동
                for i in range(int(distance)):
                        start[0] += 1
                        bat[start[0]][start[1]] = 1
                        area -= 1 # 북쪽이나 남쪽 둘 중 하나를 빼줌
        elif direct == "2": # 서쪽으로 이동
                for i in range(int(distance)):
                        start[1] -= 1
                        bat[start[0]][start[1]] = 1
        elif direct == "1": # 동쪽으로 이동
                for i in range(int(distance)):
                        start[1] += 1
                        bat[start[0]][start[1]] = 1

for i in range(499-51, 501):
        for j in range(499-161, 501):
                print(bat[i][j], end="")
        print()
# input에 따라 다 체크했으면 그 1로 만든 테두리에 따른 내부 개수를 다 센다.
for j in range(1000):
        check = starti = endi = 0
        for i in range(1000):
                if check == 0 and bat[i][j] == 1:
                        # 다음 1을 찾을 때까지
                        starti = i
                        check = 1
                elif check == 1 and bat[i][j] == 1:
                        endi = i
        area += endi - starti
        
print(area*fruit)
"""

# visual studio는 실행시 ctrl + f5
