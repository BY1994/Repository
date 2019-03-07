maxj, maxi = list(map(int, input().split()))
storenum = int(input())
stores = []
for s in range(storenum):
    stores.append(list(map(int, input().split())))
myloca = list(map(int, input().split()))

ans = 0
if myloca[0] == 1: # 북쪽
    for s in range(storenum):
        # 왼쪽으로 갔을 때와 오른쪽으로 갔을 때
        if stores[s][0] == 1: # 나랑 같은 방향
            ans += abs(myloca[1] - stores[s][1])

        elif stores[s][0] == 2:
            left = myloca[1] + maxi + stores[s][1]
            right = maxj-myloca[1] + maxi + maxj-stores[s][1]
            ans += min(left, right)
        elif stores[s][0] == 3:
            left = myloca[1] + stores[s][1]
            ans += left
        elif stores[s][0] == 4:
            right = maxj-myloca[1] + stores[s][1]
            ans += right # 아니 이걸 왜 빼먹었지


elif myloca[0] == 2: # 남쪽
    for s in range(storenum):
        # 내 방향
        if stores[s][0] == 2:
            ans += abs(myloca[1] - stores[s][1])

        elif stores[s][0] == 1:
            left = myloca[1] + maxi + stores[s][1]
            right = maxj - myloca[1] + maxi + maxj - stores[s][1]
            ans += min(left, right)
        elif stores[s][0] == 3:
            left = myloca[1] + maxi - stores[s][1]
            ans += left
        elif stores[s][0] == 4:
            right = maxj - myloca[1] + maxi - stores[s][1]
            ans += right # 여기도


elif myloca[0] == 3: # 서쪽
    for s in range(storenum):
        # 내 방향
        if stores[s][0] == 3:
            ans += abs(myloca[1] - stores[s][1])

        elif stores[s][0] == 1:
            right = myloca[1] + stores[s][1]
            ans += right
        elif stores[s][0] == 2:
            left = maxi - myloca[1] + stores[s][1]
            ans += left
        elif stores[s][0] == 4:
            left = maxi - myloca[1] + maxj + maxi - stores[s][1]
            right = myloca[1] + maxj + stores[s][1]
            ans += min(left, right)



elif myloca[0] == 4: # 동쪽
    for s in range(storenum):
        # 내 방향
        if stores[s][0] == 4:
            ans += abs(myloca[1] - stores[s][1])

        elif stores[s][0] == 1:
            right = myloca[1] + maxj - stores[s][1]
            ans += right
        elif stores[s][0] == 2:
            left = maxi - myloca[1] + maxj - stores[s][1]
            ans += left
        elif stores[s][0] == 3:
            left = myloca[1] + maxj + stores[s][1]
            right = maxi - myloca[1] + maxj + maxi - stores[s][1]
            ans += min(left, right) # 얼라 이거 없는데 답 맞았다....


print(ans)

"""
# 틀렸습니다
마지막에 내기 전에 오류 있는지 확인하려고 left랑 right만 열심히 봤는데,
ans에 더하기를 안 한게 문제였다 ㅠㅠㅠ
"""