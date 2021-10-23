"""
Atcoder 224 C
"""

# python 3 time limit
# pypy3 ac

def diff(a, b):
    diffx = coor[a][0] - coor[b][0]
    diffy = coor[a][1] - coor[b][1]

    if diffx == 0:
        return 10**9 +1
    if diffy == 0:
        return 0
    return diffy / diffx

N = int(input())
coor = []
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    coor.append([x, y])

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if diff(k, j) != diff(j, i):
                ans += 1

print(ans)            
