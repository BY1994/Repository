"""
11432 Candy Bombers

기본 이분매칭 문제
Each data set should be followed by a blank line.
-> 이것 때문에 한 번 틀림
문제 예제에는 tc 1개만 나와있어서
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    global plane, visited, pilot
    for i in range(1,plane[cur][0]+1):
        _next = plane[cur][i]-1
        if visited[_next]: continue
        visited[_next] = 1
        if pilot[_next] == 0 or dfs(pilot[_next]-1):
            pilot[_next] = cur+1
            return True
    return False

for tc in range(int(input())):
    m, n = map(int, input().split())
    visited = [0]*m
    pilot = [0]*m
    plane = []
    for i in range(n):
        plane.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(m):
            visited[j] = 0
        if dfs(i): ans += 1
    print(f"Data Set {tc+1}:")
    print(ans)
    print()
