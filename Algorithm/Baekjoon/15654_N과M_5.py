"""
15654 N 과 M 5

백트래킹
"""

import sys
input = sys.stdin.readline

def dfs(cur, depth):
    global N, M
    if depth == M:
        print(*result)
        return
    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        result[depth] = numbers[i]
        dfs(i, depth+1)
        visited[i] = 0

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * N
result = [0] * M
for i in range(N):
    visited[i] = 1
    result[0] = numbers[i]
    dfs(i, 1)
    visited[i] = 0
