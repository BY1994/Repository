"""
17481 최애 정하기

기본 이분 매칭
이름을 숫자로 변환하기 위해서 해시 필요함
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    for i in request[cur]:
        if visited[i]: continue
        visited[i] = 1
        if select[i] == 0 or dfs(select[i]-1):
            select[i] = cur+1
            return True
    return False

N, M = map(int, input().split())
girl = {}
visited = [0]*M
select = [0]*M
for i in range(M):
    girl[input()] = i
request = [[] for i in range(N)]
for i in range(N):
    names = input().split()
    for name in names[1:]:
        request[i].append(girl[name])
ans = 0
for i in range(N):
    for j in range(M):
        visited[j] = 0
    if dfs(i): ans += 1

if ans == N:
    print("YES")
else:
    print("NO")
    print(ans)
