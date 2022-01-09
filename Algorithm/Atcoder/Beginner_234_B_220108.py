# 234 B

import math

N = int(input())
dots = []
for i in range(N):
    dots.append(list(map(int, input().split())))

ans = 0.0
for i in range(N):
    for j in range(i+1, N):
       cur = math.sqrt(abs(dots[i][0]-dots[j][0])**2 + abs(dots[i][1]-dots[j][1])**2)
       if ans < cur:
           ans = cur
print(ans)
#print(f'{ans:.6f}')
