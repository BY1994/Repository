"""
11180 Paintball

이분매칭
N 명의 사람들을 매칭시키기
1과 3이 서로를 볼 수 있어도
1 -> 3 일 때, 3 -> 2 이런 식일 수 있음.
서로를 매칭해도 되지만 다른 사람들 매칭해도 됨
"""

import sys
sys.setrecursionlimit(10**6)

# function for bipartite matching
def dfs(cur):
    for i in request[cur]:
        if visited[i]: continue
        visited[i] = 1
        if shoot[i] == 0 or dfs(shoot[i]-1):
            shoot[i] = cur+1
            return True
    return False

# 1. Initialization & Input
N, M = map(int, input().split())
request = [[] for i in range(N)]
shoot = [0]*N
visited = [0]*N
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    request[a-1].append(b-1)
    request[b-1].append(a-1)

# 2. Bipartite matching
for i in range(N):
    for j in range(N):
        visited[j] = 0
    if dfs(i):
        ans += 1

# 3. Print answer
if ans != N:
    print("Impossible")
else:
    for i in range(N):
        print(shoot[i])
