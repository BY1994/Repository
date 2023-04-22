"""
2188 축사 배정

대표적인 이분 매칭 문제
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    for i in range(1,request[cur][0]+1):
        _next = request[cur][i]-1
        if visited[_next] == 0:
            visited[_next] = 1
            if match[_next] == 0 or dfs(match[_next]-1):
                match[_next] = cur+1
                return True
    return False

ans = 0
N, M = map(int, input().split())
visited = [0]*M
match = [0]*M
request = []
for i in range(N):
    S = list(map(int, input().split()))
    request.append(S)
for i in range(N):
    for j in range(M):
        visited[j] = 0
    if dfs(i):
        ans += 1
print(ans)
