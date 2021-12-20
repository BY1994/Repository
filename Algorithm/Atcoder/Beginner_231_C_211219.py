def dfs(cur, depth):
    global N, M,flag
    if depth >= N:
        correctB = []
        for i in range(M):
            correctB.append(sorted([permutation[B[i][0]-1]+1, permutation[B[i][1]-1]+1]))
        correctB.sort()
        if A == correctB:
            flag = 1
        return
    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        permutation[depth] = i
        dfs(i, depth+1)
        visited[i] = 0
    return

N, M = map(int, input().split())
A = []
B = []
degree = [0] * N
degree2 = [0] * N
for _ in range(M):
    A.append(list(map(int, input().split())))
    degree[A[_][0]-1] += 1
    degree[A[_][1]-1] += 1
for _ in range(M):
    B.append(list(map(int, input().split())))
    degree2[B[_][0]-1] += 1
    degree2[B[_][1]-1] += 1

A.sort()
flag = 0
permutation = [0] * N
visited = [0] * N
# permutation

for i in range(N):
    visited[i] = 1
    permutation[0] = i
    dfs(i, 1)
    visited[i] = 0

if flag == 1:
    print("Yes")
else:
    print("No")



# wrong answer
"""
def dfs(cur, depth):
    global N, M,flag
    if depth >= N:
        for i in range(N):
            if degree[i] != degree2[permutation[i]]: break
        else:
            flag = 1
        return
    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        permutation[depth] = i
        dfs(i, depth+1)
        visited[i] = 0
    return

N, M = map(int, input().split())
A = []
B = []
degree = [0] * N
degree2 = [0] * N
for _ in range(M):
    A.append(list(map(int, input().split())))
    degree[A[_][0]-1] += 1
    degree[A[_][1]-1] += 1
for _ in range(M):
    B.append(list(map(int, input().split())))
    degree2[B[_][0]-1] += 1
    degree2[B[_][1]-1] += 1

flag = 0
permutation = [0] * N
visited = [0] * N
# permutation

for i in range(N):
    visited[i] = 1
    permutation[0] = i
    dfs(i, 1)
    visited[i] = 0

if flag == 1:
    print("Yes")
else:
    print("No")
"""

"""
def dfs(cur, depth):
    global N, M,flag
    if depth >= N:
        for i in range(M):
            if A[i][0] != permutation[B[i][0]-1]+1: break
            if A[i][1] != permutation[B[i][1]-1]+1: break
        else:
            flag = 1
        return
    for i in range(N):
        if visited[i] == 1: continue
        visited[i] = 1
        permutation[depth] = i
        dfs(i, depth+1)
        visited[i] = 0
    return

N, M = map(int, input().split())
A = []
B = []
for _ in range(M):
    A.append(list(map(int, input().split())))
for _ in range(M):
    B.append(list(map(int, input().split())))

flag = 0
permutation = [0] * N
visited = [0] * N
# permutation

for i in range(N):
    visited[i] = 1
    permutation[0] = i
    dfs(i, 1)
    visited[i] = 0

if flag == 1:
    print("Yes")
else:
    print("No")
"""





# 정답
# https://atcoder.jp/contests/abc232/editorial/3152
"""
import itertools
n, m = map(int, input().split())
a = [[False] * n for _ in range(n)]
b = [[False] * n for _ in range(n)]
for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  a[u][v] = a[v][u] = True
  
for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  b[u][v] = b[v][u] = True
  
ans = False
for p in itertools.permutations(range(n)):
  ok = True
  for i in range(n):
    for j in range(n):
      if a[i][j] != b[p[i]][p[j]]:
      	ok = False
  if ok:
    ans = True
print("Yes" if ans else "No")
"""
