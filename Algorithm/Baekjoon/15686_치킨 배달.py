"""
15686 치킨 배달

2019.04.12 PBY 최초 작성
"""

N, M = map(int, input().split())
city = []
chicken = 0
chickens = []
for i in range(N):
    temp = list(map(int, input().split()))
    city.append(temp)
    for j in range(N):
        if temp[j] == 2:
            chicken += 1
            chickens.append([i, j])

minsum = 2501*2501

# 각 치킨집에서부터 치킨 거리를 잰다
from itertools import combinations
for comb in combinations(range(chicken), M):
    dist = [[2501 for _ in range(N)] for __ in range(N)]
    # comb에 있는 하나씩이 chickens의 좌표
    for c in comb:
        for i in range(N):
            for j in range(N):
                if city[i][j] == 1: # 집이면 거기의 거리를 잰다
                    tempdist = abs(chickens[c][0]-i) + abs(chickens[c][1]-j)
                    if dist[i][j] > tempdist:
                        dist[i][j] = tempdist
    # comb를 다 돌고 났을 때 치킨 거리 합 최소
    tempsum = 0
    for i in range(N):
        for j in range(N):
            if dist[i][j] < 2501:
                tempsum += dist[i][j]

    # 매 집을 다 최소거리로 갱신
    # 갱신 후 전체 최소값과 비교
    if minsum > tempsum:
        minsum = tempsum

print(minsum)