"""
17254 키보드 이벤트

input)
3 5
1 0 A
2 1 P
1 2 L
2 4 E
3 0 P

2019.06.25 PBY 최초 작성
"""

N, M = map(int, input().split())
keyboards = [[0]*3 for _ in range(M)]
for i in range(M):
    a, b, keyboards[i][2] = input().split()
    keyboards[i][0] = int(a); keyboards[i][1] = int(b);

keyboards.sort(key = lambda x: (x[1], x[0]))

for i in range(M):
    print(keyboards[i][2], end='')
