def fillBlock(remain):
    global minvalue, N, possible

    if remain == 0:  # 모든 색종이 다 채웠으면
        possible = 1
        if minvalue > 25 - sum(blocks):
            minvalue = 25 - sum(blocks)
        return

    # 채우기 시작할 지점 선택
    flag = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                flag = 1
                nextx, nexty = i, j
                break
        if flag == 1:
            break

    # 그 지점부터 가능한 색종이 크기 선택
    for size in range(5, 0, -1):
        flag = 0
        for x in range(nextx, nextx + size):
            for y in range(nexty, nexty + size):
                if x >= N or y >= N or board[x][y] == 0:  # 색종이가 없으면
                    flag = 1
                    break
            if flag == 1:
                break
        else:  # break가 걸리지 않으면
            if blocks[size - 1] > 0:  # 색종이가 남아있을 때
                blocks[size - 1] -= 1
                # 색종이 덮기
                for x in range(nextx, nextx + size):
                    for y in range(nexty, nexty + size):
                        board[x][y] = 0
                fillBlock(remain - size * size)
                blocks[size - 1] += 1
                for x in range(nextx, nextx + size):
                    for y in range(nexty, nexty + size):
                        board[x][y] = 1


N = 10
blocks = [5, 5, 5, 5, 5]

minvalue = 25 # 모든 색종이 다 썼을 때

board = []
ncolors = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
    ncolors += sum(temp)

possible = 0
fillBlock(ncolors)

if possible == 0:
    print(-1)
else:
    print(minvalue)

