"""
BOJ 1773 폭죽쇼

2019.06.10 최초작성
"""


N, C = map(int, input().split())
time = [0]*C
for n in range(N):
    student = int(input())
    for t in range(1, C//student+1):
        time[student*t-1] = 1

print(sum(time))

