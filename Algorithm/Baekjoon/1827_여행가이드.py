"""

cos theta 가 직각 삼각형의 아랫변
sin theta가 직각 삼각형의 세로...!
"""

# 근의 공식 몇 번 틀렸고 ㅠㅠ
# 그 다음에 people을 원래 값에서 순열마다 자꾸 더하게 해서!!!! 값이 자꾸 바뀐채로 다음 순열을 돌았따!!!

import copy
N = int(input())
mySpeed = float(input())
people_origin = []
for _ in range(N):
    people_origin.append(list(map(float, input().split())))

totalminvalue = 10**6
# 내 시작 좌표
import math
# 모든 순열을 다 가봐야한다.
import itertools
for i in itertools.permutations(range(N)):
    # 매번 복사하기
    people = copy.deepcopy(people_origin) # 이거 대신 밑에서 totalt를 빼면 되는 거 아닌가?
    Iam = [0, 0]
    totalt = 0
    maxvalue = 0
    # 잡으러 갈 때마다 그 만큼의 시간이 지나야한다.
    
    # 0, 1, 2, ... N번째 순으로 한 명씩 잡으러 간다.
    # 내가 0번째 사람을 잡으로 갔을 때의 위치는, 그 사람이 이동하다가 내가 따라잡는 순간
    # 지금 나와 떨어진 거리를 속도의 차이로 언제 후에 잡을 수 있는지
    for j in i: # 몇 번째 사람을 잡음
        # 그사람은 totalt만큼 좌표가 이동해있다.
        people[j][0] += totalt*people[j][2]*math.cos(people[j][3])
        people[j][1] += totalt*people[j][2]*math.sin(people[j][3])
        
        # 그 사람이 몇 t 후에 나와 만나는지
        a = people[j][2]**2 - mySpeed**2
        b = 2*people[j][2]*(math.cos(people[j][3])*(people[j][0]-Iam[0]) + math.sin(people[j][3])*(people[j][1]-Iam[1]))
        c = (people[j][0]-Iam[0])**2 + (people[j][1]-Iam[1])**2
#        b = 2*people[j][2]*math.cos(people[j][3])*(people[j][0]-Iam[0]) + 2*people[j][2]*math.sin(people[j][3])*(people[j][1]-Iam[1])
#        b = 2*people[j][2]*(people[j][0]*math.cos(people[j][3]) + people[j][1]*math.sin(people[j][3]))
#        c = people[j][0] ** 2 + people[j][1] ** 2 - 2*people[j][0]*Iam[0] - 2*people[j][1]*Iam[1] + Iam[0]**2 + Iam[1]**2
        
        tvalue1 = (-b + math.sqrt(b**2 - 4*a*c) ) / (2*a)
        tvalue2 = (-b - math.sqrt(b**2 - 4*a*c) ) / (2*a)

        if tvalue1 >= tvalue2:
            # 그러면 tvalue2 선택
            if tvalue2 >= 0:
                t = tvalue2
            else: t = tvalue1
            
        elif tvalue1 < tvalue2:
            # 그러면 tvalue1 선택
            if tvalue1 >= 0:
                t = tvalue1
            else: t = tvalue2
        else:
            print("그런 경우가 있으면 안 되는데")

        # 내 좌표 업데이트 ( 내가 잡은 그 사람의 좌표 )
        Iam[0] = people[j][0] + people[j][2] * t * math.cos(people[j][3])
        Iam[1] = people[j][1] + people[j][2] * t * math.sin(people[j][3])
        totalt += t
        
        # 그 사람을 잡음. 그 사람이 그 때부터 버스로 간다.
        # 버스까지 가는데 걸리는 시간은 거기서 버스까지 거리 / 속도
        curvalue = totalt + math.sqrt(Iam[0] **2 + Iam[1] ** 2) / people[j][2]
        if maxvalue < curvalue:
            maxvalue = curvalue
        # 다음 사람 잡으러 감  -> 다음 for문
        
    if totalminvalue > maxvalue:
        totalminvalue = maxvalue

print(round(totalminvalue))        
