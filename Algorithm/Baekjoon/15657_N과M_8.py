"""
15657 N과 M 8

백트래킹
"""

import sys
input = sys.stdin.readline

def dfs(cur, depth):
    global N,M
    if depth == M:
        print(*visited)
        return
    for i in range(cur, N):
        visited[depth] = numbers[i]
        dfs(i, depth+1)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * M
for i in range(N):
    visited[0] = numbers[i]
    dfs(i, 1)
