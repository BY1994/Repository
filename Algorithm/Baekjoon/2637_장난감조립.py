"""
2637 장난감 조립
"""

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
indegree = [0] *N
total = [[0 for _ in range(N)] for __ in range(N)]
need = [[0 for _ in range(N)] for __ in range(N)]

for i in range(M):
    _input = list(map(int, input().split()))
    graph[_input[1]-1].append(_input[0]-1)
    indegree[_input[0]-1] += 1
    need[_input[0]-1][_input[1]-1] = _input[2]
            
q = []
# 기본 부품
default = []
for i in range(N):
    if indegree[i] == 0:
        q.append(i)
        default.append(i)
        total[i][i] += 1

while q:
    cur = q.pop(0)
    
    for node in graph[cur]:
        indegree[node] -= 1
        node_need = need[node][cur]
        for j in range(N):
            total[node][j] += total[cur][j] * node_need
        if indegree[node] == 0:
            q.append(node)


default.sort()
for i in default:
    print(i+1, total[N-1][i])
