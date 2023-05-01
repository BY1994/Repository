"""
11375 열혈강호

기본 이분매칭

dfs 내에서 매번 [1:] 자르는 걸 넣었더니 시간 초과가 났다.
그래서 미리 잘라두는 것으로 변경하였다.
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    for i in request[cur]:
        if visited[i-1]: continue
        visited[i-1] = 1
        if result[i-1] == 0 or dfs(result[i-1]-1):
            result[i-1] = cur+1
            return True
    return False

N, M = map(int, input().split())
request = []
visited = [0]*M
result = [0]*M
ans = 0
for i in range(N):
    work = list(map(int, input().split()))
    request.append(work[1:])
for i in range(N):
    for j in range(M):
        visited[j] = 0
    if dfs(i): ans += 1
print(ans)
