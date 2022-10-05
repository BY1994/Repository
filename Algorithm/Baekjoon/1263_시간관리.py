"""
1263 시간 관리

그리디 알고리즘
일을 연속해서 해야한다는 조건이 없음
범위 안에만 하면 되기 때문에
마감일 제일 뒤에서부터 순서대로 배정해도 됐다
"""

N = int(input())
work = []
for i in range(N):
    T, S = map(int, input().split())
    work.append([S, T])
work.sort(key=lambda x: -x[0])

limit = 1000000
for i in range(N):
    limit = min(limit, work[i][0]) - work[i][1]

if limit < 0:
    print(-1)
else:
    print(limit)
