import sys
sys.stdin = open('2636_input.txt', 'r')

# input
height, width = list(map(int, input().split()))

# 치즈 판 만들기
Cheese = []
for _ in range(height):
    Cheese.append(input().split())

# 시작점을 저장해두고 거기서 다시 돌도록 하자.


# DFS로 치즈 찾아 가고
def findCheese(nextx, nexty):
    global width
    global height

    # print(nextx, nexty)
    visited[nextx][nexty] = 1

    if Cheese[nextx][nexty] == '1':
        Cheese[nextx][nexty] = '2'
        start.append([nextx, nexty])

    elif Cheese[nextx][nexty] == '0': # 런타임 에러가 혹시 '2' 인 경우 다시 사방으로 찾아서인가?
        if nextx-1 >= 0 and not visited[nextx-1][nexty]:
            findCheese(nextx-1, nexty)
        if nextx+1 < height and not visited[nextx+1][nexty]:
            findCheese(nextx+1, nexty)
        if nexty-1 >= 0 and not visited[nextx][nexty-1]:
            findCheese(nextx, nexty-1)
        if nexty+1 < width and not visited[nextx][nexty+1]:
            findCheese(nextx, nexty+1)


# 체크된 치즈 지우고
def deleteCheese():
    for i in range(height):
        for j in range(width):
            if Cheese[i][j] == '2':
                Cheese[i][j] = '0'
                # visited[i][j] = 0 # 다음에 방문 안 한 곳부터 시작할 수 있도록

# 남은 치즈 개수 세고
def countCheese():
    cnt = 0
    for i in range(height):
        for j in range(width):
            if Cheese[i][j] == '1':
                cnt += 1
    return cnt

cnt = countCheese()
cheesestate = [[cnt, 0]]

visited = [[0 for _ in range(width)] for __ in range(height)]
start = [[0, 0]]
while True:
    # 먼저 치즈 개수 없애봄

    """
        for i in range(height):
            for j in range(width):
                if Cheese[i][j] == '0' and not visited[i][j]: # 방문한 곳 처리를 안 해서 재귀함수 스택 오버플로우 난 듯
                    break
            if Cheese[i][j] == '0' and not visited[i][j]:
                break
    """
    for i in range(len(start)):
        findCheese(start[i][0], start[i][1])
    start = start[i+1:][:]
    # findCheese(0, 0)

    # 체크된 치즈 지우기
    deleteCheese()

    # 남은 치즈 개수 세서 업데이트
    cnt = countCheese()
    if cnt == 0:
        break

    cheesestate.append([cnt, cheesestate[-1][1]+1]) # depth 하나씩 늘려봄

print(cheesestate[-1][1]+1)
print(cheesestate[-1][0])


"""
런타임 에러 => 재귀함수 호출 시 깊이가 너무 깊어서 계속 에러가 났다.
1) 이전에 2로 체크한 것부터 시작해서 재귀를 너무 많이 부르지 않도록 했다. (queue 형태 리스트에 넣어두었다)
2) visited는 매번 새로고침하지 않고 계속 공유하도록 했다.
"""

"""
    if nextx < 0 or nextx >= width or nexty < 0 or nexty >= height or Cheese[nextx][nexty] == '2' :
        return 0
    elif Cheese[nextx][nexty] == '1':
        Cheese[nextx][nexty] = '2'
    elif : # 0인 경우 => visited 체크 안 해줄 때의 코드 => 재귀를 계속 들어가서 죽음
        findCheese(nextx-1, nexty)
        findCheese(nextx, nexty-1)
        findCheese(nextx+1, nexty)
        findCheese(nextx, nexty+1)
"""