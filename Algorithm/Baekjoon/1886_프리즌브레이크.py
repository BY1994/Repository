"""
1886 프리즌 브레이크

이분매칭 다이아 문제 풀어보려고 했는데,
한 사람이 한 문과 매칭이 아니라,
한 사람이 한 문의 한 타임과 매칭이기 때문에
이분매칭 코드가 복잡하다.

2023.05.03 구현 실패
"""

# input
N, M = map(int, input().split())
_exit = []
miro = []
miro2 = [[0 for i in range(m)] for j in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
pcount = 0
vcount = 0
ecount = 0
for i in range(N):
    miro.append(input())
    for j in range(M):
        if miro[i][j] == 'D':
            _exit.append([i,j])
            ecount += 1
        elif miro[i][j] == '.':
            miro2[i][j] = pcount
            pcount += 1
people = [[] for i in range(pcount)]

# bfs
for ex, ey in _exit: # 'D'
    qs, qe = 0, 1
    vcount += 1
    q = [[ex, ey, 0]]
    while qs < qe:
        cx, cy, d = q[qs]
        qs += 1
        for nx, ny in (cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1):
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if miro[nx][ny] == 'X': continue
            if visited[nx][ny] == vcount: continue
            visited[nx][ny] = vcount
            people[miro2[nx][ny]].append([0, d+1])

# bipartite matching
# 여러 사람 -> 한 문의 한 타임과 매칭
# 이 부분 잘못 생각함...
def dfs(cur):
    for e, d in people[cur]:
        if exit_visited[e]: continue
        if exit_time[e] < d: continue

ans = 0
exit_visited = [0]*ecount
exit_matching = [0]*ecount
exit_time = [0]*ecount
for i in range(pcount):
    for j in range(ecount):
        exit_visited[j] = 0
    if dfs(i):
        ans += 1
if ans == pcount:
    print(max(exit_time))
else:
    print("impossible")
