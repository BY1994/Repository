"""
1940 주몽

2 2 7 7 이런 경우는 어떻게 되나 고민했는데
지문에서 값이 고유하다고 했기 때문에 문제가 안 됨
"""

N = int(input())
M = int(input())
material = list(map(int, input().split()))
material.sort()

ans = 0
p1 = 0
p2 = N-1
while p2 < N and p1 < p2:
    if material[p1] + material[p2] == M:
        ans += 1
        p1 += 1
    elif material[p1] + material[p2] > M:
        p2 -= 1
    else:
        p1 += 1

print(ans)    
