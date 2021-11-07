"""
Atcoder 226 C


반례
누적해버려서...문제임...
3
3 0
5 1 1
7 2 1 2

이거 memo 값 출력해보니 3, 8, 18 나옴....
"""

import sys
sys.setrecursionlimit(1000000000)

def dfs(cur):
    if memo[cur] != -1:
        return memo[cur]
    
    temp = time[cur]
    for parent in prev[cur]:
        if memo[parent-1] == -1: # use as visited
            temp += dfs(parent-1)

    memo[cur] = temp

    return temp
        

N = int(input())
time = [0] * N
prev = [[] for _ in range(N)]
memo = [-1] * N

for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    prev[i].extend(_input[2:])

print(dfs(N-1))

# 위상정렬, 똑같은 반례에서 걸림
"""
N = int(input())
time = [0] * N
graph = [[] for _ in range(N)]
indegree = [0] * N
ans = [0] * N

for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    for j in range(_input[1]):
        graph[_input[2+j]-1].append(i)
        indegree[i] += 1

q = []
for i in range(N):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.pop(0)
    ans[cur] += time[cur]

    for node in graph[cur]:
        indegree[node] -= 1
        ans[node] += ans[cur]
        if indegree[node] == 0:
            q.append(node)

print(ans[N-1])
"""

"""
import sys
sys.setrecursionlimit(1000000000)

def dfs(cur):
    if memo[cur] != -1:
        return memo[cur]
    
    temp = time[cur]
    for parent in prev[cur]:
        temp += dfs(parent-1)

    memo[cur] = temp

    return temp
        

N = int(input())
time = [0] * N
prev = [[] for _ in range(N)]
memo = [-1] * N

for i in range(N):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    if _input[1] == 0:
        memo[i] = time[i]
    prev[i].extend(_input[2:])

print(dfs(N-1))

"""
