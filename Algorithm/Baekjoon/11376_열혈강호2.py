"""
11376 열혈강호 2

2023.04.29
python3 시간초과
pypy3 메모리초과

알고리즘 수정 필요
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    for i in request[cur]:
        if visited[i-1]: continue
        visited[i-1] = 1
        if result[i-1] == cur+1: continue
        if result[i-1] == 0 or dfs(result[i-1]-1):
            result[i-1] = cur+1
            return True
    return False

N, M = map(int, input().split())
visited = [0]*M
result = [0]*M
request = []
for i in range(N):
    work = list(map(int, input().split()))
    request.append(work[1:])
ans = 0
for i in range(N):
    for j in range(M):
        visited[j] = 0
    if dfs(i): ans += 1
    for j in range(M):
        visited[j] = 0
    if dfs(i): ans += 1
print(ans)
