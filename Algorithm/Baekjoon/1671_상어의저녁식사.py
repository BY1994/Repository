"""
1671 상어의 저녁식사

한 상어가 다른 상어의 크기, 속도, 지능보다 같거나 크면 먹을 수 있다.
완전히 같을 때 중복되지 않도록 하기 위해서 아래 게시글에서 사용한 방법처럼
인덱스가 큰 상어가 작은 상어를 먹을 수 있도록 처리했다.
(정말 좋은 아이디어다...)
https://mangu.tistory.com/154
"""

import sys
sys.setrecursionlimit(10**6)

N = int(input())
shark = []
visited = [0]*N
result = [0]*N
request = [[] for i in range(N)]

def dfs(cur):
    for i in request[cur]:
        if visited[i]: continue
        visited[i] = 1
        if result[i] == cur+1: continue
        if result[i] == 0 or dfs(result[i]-1):
            result[i] = cur+1
            return True
    return False

for i in range(N):
    shark.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if i == j: continue
        if shark[i][0] == shark[j][0] and shark[i][1] == shark[j][1] and shark[i][2] == shark[j][2]:
            if i > j:
                request[i].append(j)
        elif shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            request[i].append(j)
        
ans = 0
for i in range(N):
    for j in range(N):
        visited[j] = 0
    if dfs(i): ans += 1

    for j in range(N):
        visited[j] = 0
    if dfs(i): ans += 1
print(N-ans)
