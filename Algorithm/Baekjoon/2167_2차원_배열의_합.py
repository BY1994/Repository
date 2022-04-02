"""
2167 2차원 배열의 합


(1) prefix
A B
C D

D 는 0, 0 에서 1, 1 까지의 합
D = B+C-A(공통)+D 지점의 값

(2) sum (i, j)~(x, y)
A B
C D

D는 (0,0)~(x,y)
(i,j)~(x,y) 의 값을 구하려면 D에서 B, C 빼고 A 더하면 됨
"""
import sys
input = sys.stdin.readline

arr = []
prefix = [[0 for i in range(301)] for j in range(301)]
N, M = map(int, input().split())
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + arr[i][j]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1])
