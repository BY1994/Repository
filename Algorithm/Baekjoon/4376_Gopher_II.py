"""
4376 Gopher II
2191 들쥐의 탈출과 동일한 문제

기본 이분매칭 + 거리 사전에 계산해야함
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    global request, visited
    for i in request[cur]:
        if visited[i]: continue
        visited[i] = 1
        if result[i] == 0 or dfs(result[i]-1):
            result[i] = cur+1
            return True
    return False

while True:
    try:
        N, M, S, V = map(int, input().split())
        mouse = []
        tunnel = []
        for i in range(N):
            x, y = map(float, input().split())
            mouse.append([x,y])
        for i in range(M):
            x, y = map(float, input().split())
            tunnel.append([x,y])
        visited = [0]*M
        result = [0]*M
        request = [[] for i in range(N)]
        S = S*S
        V = V*V
        ans = 0
        for i in range(N):
            for j in range(M):
                if (mouse[i][0]-tunnel[j][0])**2 + (mouse[i][1]-tunnel[j][1])**2 <= S*V:
                    request[i].append(j)
        for i in range(N):
            for j in range(M):
                visited[j] = 0
            if dfs(i):
                ans += 1
        print(N-ans)
    except:
        break
