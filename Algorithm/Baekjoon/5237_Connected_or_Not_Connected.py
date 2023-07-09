"""
5237 Connected or Not Connected

DFS
"""

def recur(_cur):
    global visited, edge
    for _next in edge[_cur]:
        if visited[_next] == 0:
            visited[_next] = 1
            recur(_next)
    
for tc in range(int(input())):
    line_ = list(map(int,input().split()))
    n = line_[0]
    edge = [[] for i in range(n)]
    visited = [0]*n
    for k in range(2, (line_[1]+1)*2, 2):
        a = line_[k]-1
        b = line_[k+1]-1
        edge[a].append(b)
        edge[b].append(a)
    visited[0] = 1
    recur(0)
    for v in visited:
        if v == 0:
            print("Not connected.")
            break
    else:
        print("Connected.")
