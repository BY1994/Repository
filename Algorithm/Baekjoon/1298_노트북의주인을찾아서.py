"""
1298 노트북의 주인을 찾아서

이분 매칭
https://blog.naver.com/ndb796/221240613074

N 과 M 의 의미를 제대로 이해하지 않고 있어서 인덱스 에러 발생
사람도 N 명, 노트북도 N 명이라고 문제에서 주어짐
M 은 사람과 노트북의 연결 관계의 수였다.
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    for c in request[cur]:
        if visited[c]:
            continue
        visited[c] = 1
        if notebook[c] == 0 or dfs(notebook[c]-1):
            notebook[c] = cur+1
            return True
    return False

N, M = map(int, input().split())
request = [[] for i in range(N)]
visited = [0]*N
notebook = [0]*N
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    request[a-1].append(b-1)
for i in range(N):
    for j in range(N):
        visited[j] = 0
    if dfs(i):
        ans += 1
print(ans)
