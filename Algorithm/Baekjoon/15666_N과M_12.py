"""
15666 N과 M 12
"""

import sys
input = sys.stdin.readline

def dfs(cur, depth):
    global N, M
    if depth == M:
        print(*visited)
        return

    for i in range(cur, N):
        num = numbers[i]
        visited[depth] = num
        dfs(i, depth+1)

origin_N, M = map(int, input().split())
origin_input = list(map(int, input().split()))
visited = [0]*M
count = [0] * 10001
numbers = [0]*origin_N
N = 0

for i in origin_input:
    count[i] += 1

for i in range(1, 10001):
    if count[i] > 0:
        numbers[N] = i
        N += 1

for i in range(N):
    num = numbers[i]
    visited[0] = num
    dfs(i, 1)
