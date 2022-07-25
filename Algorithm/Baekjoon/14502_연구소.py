"""
14502 연구소

Brute Force
BFS

보통 벽 3개를 세울 때 재귀함수를 쓰는데,
3개 밖에 안 되니까 재귀함수 안 쓰고 for 문으로 구현하고 싶어서 했더니
아래와 같이 인덱스 처리가 좀 불편해졌다.

질문 게시판
이 문제의 시간복잡도를 계산하면서 비슷한 고민을 해봤기 때문에 아래 질문에 답변을 남겨보았다.
https://www.acmicpc.net/board/view/94122

이중 for 문을 많이 쓰게 되면 64 씩 곱해지니까 금방 1억이 넘어간다

=============================
2021.12.04 첫 시도 (미완성)
2022.07.25 통과
"""

N, M = map(int, input().split())
lab = []
ans = 0
visited = [[0 for i in range(M)] for j in range(N)]
visit_count = 0
for i in range(N):
    lab.append(list(map(int, input().split())))

total_size = N*M
empty = 0
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty += 1
        elif lab[i][j] == 2:
            virus.append((i, j))

virus_count = len(virus)
empty -= 3 # 벽 3개 빼기

for w1 in range(total_size):
    if lab[w1//M][w1%M] != 0:
        continue
    for w2 in range(w1+1, total_size):
        if lab[w2//M][w2%M] != 0:
            continue
        for w3 in range(w2+1, total_size):
            if lab[w3//M][w3%M] != 0:
                continue
            remain = empty
            visit_count += 1
            visited[w1//M][w1%M] = visit_count
            visited[w2//M][w2%M] = visit_count
            visited[w3//M][w3%M] = visit_count
            qs = 0
            qe = 0
            q = []
            for i in range(virus_count):
                q.append(virus[i])
                qe += 1

            while qs < qe:
                x, y = q[qs]
                qs += 1

                if ans >= remain: # 가지치기
                    break

                for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if visited[nx][ny] == visit_count:
                        continue
                    if lab[nx][ny] == 0:
                        visited[nx][ny] = visit_count
                        q.append((nx, ny))
                        qe += 1
                        remain -= 1

            ans = max(ans, remain)

print(ans)

# 2021.12.04 (미완성 버전), 재귀로 벽 3개 세우려고 함
"""
def dfs(x, y, depth):
    if depth == 3:
        q = []
        
        # bfs
        # visited 이용
    # i, j 다음 거 dfs()

mymap = []
vind = 3
visited = [[0 for i in range(M)] for j in range(N)]
N, M = map(int, input().split())
for _ in range(N):
    mymap.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if mymap[i][j] == 0:
            mymap[i][j] = 1
            dfs(i, j, 1)
            mymap[i][j] = 0
"""
