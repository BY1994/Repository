"""
1697 숨바꼭질

BFS

런타임 에러 났을 때
5 174

반례
https://www.acmicpc.net/board/view/92318
0 100000
wrong answer:-1
answer:22

런타임 에러 해결방법
bound 처리를 해줬다. 아래 한 문장씩 추가
if nextcur <= 200000 and nextcur >= -200000:
"""

N, K = map(int, input().split())
visited = [0] * 400001

q = [[N, 0]]
qs = 0
qe = 1
visited[N + 200000] = 1

while qs < qe:
    cur, dist = q[qs]
    qs += 1

    if cur == K:
        print(dist)
        break

    nextcur = cur-1
    if nextcur <= 200000 and nextcur >= -200000:
        if visited[nextcur + 200000] == 0:
            q.append([nextcur, dist+1])
            qe += 1
            visited[nextcur + 200000] = 1

    nextcur = cur + 1
    if nextcur <= 200000 and nextcur >= -200000:
        if visited[nextcur + 200000] == 0:
            q.append([nextcur, dist+1])
            qe += 1
            visited[nextcur + 200000] = 1

    nextcur = cur*2
    if nextcur <= 200000 and nextcur >= -200000:
        if visited[nextcur + 200000] == 0:
            q.append([nextcur, dist+1])
            qe += 1
            visited[nextcur + 200000] = 1

