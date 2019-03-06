"""
2667 단지번호 붙이기

2019.03.06 PBY 최초작성
"""
import sys
sys.stdin = open('2667_input.txt','r')

N = int(input())
danji = []
visited = [[0 for _ in range(N)] for __ in range(N)]

for n in range(N):
    danji.append(input())

def findhouse(nextx, nexty):
    global danjinum
    visited[nextx][nexty] = danjinum
    if nextx - 1 >= 0 and not visited[nextx-1][nexty] and danji[nextx-1][nexty] == '1':
        findhouse(nextx-1, nexty)
    if nextx + 1 < N and not visited[nextx+1][nexty] and danji[nextx+1][nexty] == '1':
        findhouse(nextx+1, nexty)
    if nexty -1 >= 0 and not visited[nextx][nexty-1] and danji[nextx][nexty-1] == '1':
        findhouse(nextx, nexty-1)
    if nexty +1 < N and not visited[nextx][nexty+1] and danji[nextx][nexty+1] == '1':
        findhouse(nextx, nexty+1)

# 모든 1을 찾아서 시작점으로 구현
danjinum = 0
for i in range(N):
    for j in range(N):
        if danji[i][j] == '1':
            if visited[i][j] == 0: # 새로운 단지인데 아직 방문 안 했으면 단지 번호 증가시키고 BFS 시작
                danjinum += 1
                findhouse(i, j)
            # 이미 방문한 단지는 BFS를 들어가선 안 됨 => 단지 번호를 최신으로 덮어쓰게 됨

print(danjinum)
# 오름차순으로 정렬하는 거 아직 구현 안 함
danjis = []
for d in range(1, danjinum+1):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == d:
                cnt += 1
    danjis.append(cnt)

danjis.sort()
for i in danjis:
    print(i)

"""
visited에 1 체크 하는 대신 단지번호를 쓴 건 엄청 좋은 선택이었다!!!!!!!!!!
"""