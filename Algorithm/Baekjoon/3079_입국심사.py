# 2019.03.30
# 입국심사 문제
# 이분탐색

import math

N, M = map(int, input().split())
tks = []
for _ in range(N):
    tks.append(int(input()))
left = min(tks)*M//N# 0 # 모두가 가장 짧은 tk라고 가정했을 때
right = math.ceil(max(tks)*M/N)# min(tks)*M # 최소의 시간으로 M명이 다 서는 경우
people = 0
# 이진 탐색
while True:
    middle = (left+right)//2
    temppeople = people
    # tks를 돌면서 지금 시간 안에 몇 명이 들어오는지
    people = 0
    for tk in tks:
        people += middle // tk # 이 시간 안에 몇 명을 할 수 있는지
    if left > right: # 무한루프에 빠지면 left가 더 커지고, right와 middle이 계속 같다.
        ans = middle + 1
        break
    if people >= M:
        right = middle-1
    elif people < M:
        left = middle+1
print(ans)


"""
2 6
7
10

7 10
3
8
3
6
9
2
4

3 4
2
2
2

"""
