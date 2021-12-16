"""
2529 부등호

"""

def dfs(cur, depth, value):
    global N, _max, _min
    if depth > N:
        _max = max(_max, value)
        _min = min(_min, value)
        return
    for i in range(10):
        if visited[i] == 0:
            if symbol[depth-1] == '<' and cur > i: continue
            if symbol[depth-1] == '>' and cur < i: continue
            visited[i] = 1
            dfs(i, depth+1, value*10 + i)
            visited[i] = 0

_max = 0
_min = 9999999999
N = int(input())
visited = [0]*10
symbol = input().split()
for i in range(10):
    visited[i] = 1
    dfs(i, 1, i)
    visited[i] = 0
print(format(str(_max).zfill(N+1)))
print(format(str(_min).zfill(N+1)))
