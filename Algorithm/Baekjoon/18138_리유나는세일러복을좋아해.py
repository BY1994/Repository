"""
18138 리유나는 세일러복을 좋아해

기본 이분매칭
이분매칭 전에 가능한 후보들을 직접 계산해야함
흰티와 세일러 카라가 서로 가능한 관계인지 (크기 범위 안에 들어오는지)
계산해서 후보군을 만들어둬야함
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    for i in request[cur]:
        if visited[i]:
            continue
        visited[i] = 1
        if cloth[i] == 0 or dfs(cloth[i]-1):
            cloth[i] = cur+1
            return True
    return False

N, M = map(int, input().split())
Tshirt = []
Sailor = []
ans = 0
visited = [0]*M
cloth = [0]*M
request = [[] for i in range(N)]
for i in range(N):
    Tshirt.append(int(input()))
for i in range(M):
    Sailor.append(int(input())*4)
for i in range(N):
    for j in range(M):
        if Tshirt[i]*2 <= Sailor[j] <= Tshirt[i]*3:
            request[i].append(j)
        elif Tshirt[i]*4 <= Sailor[j] <= Tshirt[i]*5:
            request[i].append(j)
for i in range(N):
    for j in range(M):
        visited[j] = 0
    if dfs(i):
        ans += 1
print(ans)
