"""
16507 어두운 건 무서워

누적 합
"""
import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
picture = []
for i in range(R):
    picture.append(list(map(int, input().split())))

prefix = [[0 for i in range(C+1)] for j in range(R+1)]

for j in range(1, C+1):
    for i in range(1, R+1):
        prefix[i][j] = prefix[i-1][j] + picture[i-1][j-1]

for i in range(1, R+1):
    for j in range(1, C+1):
        prefix[i][j] += prefix[i][j-1]

for i in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    total = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1]
    print(total // ((r2-r1+1)*(c2-c1+1)))
    
