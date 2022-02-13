"""
2051

2 05 = 2 + 
20
2
0
5
1
05
51



0 의 개수
"""

def solve(l, idx_l, idx_r):
    cnt = 0
    for i in range(idx_l, idx_r):
        if l[i] == 0:
            cnt += 1
    return cnt + idx_r - idx_l

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans= 0
    for i in range(n):
        for j in range(i+1, n+1):
            ans += solve(a, i, j)
    
    print(ans)
