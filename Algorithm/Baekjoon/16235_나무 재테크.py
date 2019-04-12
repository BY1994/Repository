"""
16235 나무 재테크

2019.04.12 PBY 최초작성

"""

import copy
N, M, K = map(int, input().split())
nutrition = []
for _ in range(N):
    nutrition.append(list(map(int, input().split())))

copy_nutrition = copy.deepcopy(nutrition)

forest = [[0 for _ in range(N)] for __ in range(N)]

totaltree = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    forest[x][y][0] += 1 # 그 칸의 나무의 개수
    totaltree += 1
    forest[x][y].append(z) # 나무의 나이들 저장

time = 0
while time < K: # K년이 지난 후 남은 나무의 개수
    trees5 = [[0 for _ in range(N)] for __ in range(N)] # 5의 배수 저장하는 리스트

    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            if forest[i][j][0] > 0: # 나무가 하나라도 있으면 체크
                temp_tree = sorted(forest[i][j][1:]) # 나무들
                # 맨 왼쪽 tree부터 양분 먹고 안 되면 int(/2) 로 양분이 되어버린다
                for t in range(forest[i][j][0]):
                    if temp_tree[t] > nutrition[i][j]:
                        break
                    nutition[i][j] -= temp_tree[t]
                    temp_tree[t] += 1 # 나이를 하나 먹는다.
                    if temp_treep[t] % 5 == 0:
                        trees[i][j] += 1
                else: t += 1 # 지금 남은 나무의 개수

                # 양분 먹고 안 되면 int(/2) 로 양분이 되어버린다.
                # t가 나무의 개수
                forest[i][j] = [t] + temp_tree[:t]
                for t2 in range(t, len(temp_tree)):
                    nutrition[i][j] += int(temp_tree[t2]/2)
    # 가을
    # 나이가 5의 배수인 나무가 있으면 인접한 8개 칸에 나이가 1인 나무가 생긴다.
    for i in range(N):
        for j in range(N):
            if forest[i][j] > 0:
                # 그 개수만큼 주변 8개에 나무 추가


    # 겨울 양분 추가
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += copy_nutrition[i][j]

    time += 1
print(totaltree)