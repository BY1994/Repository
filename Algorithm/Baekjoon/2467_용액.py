"""
2467 용액

two pointer
정렬하고 가장 작은 것과 가장 큰 것을 비교했을 때,
음수라면 가장 작은 거를 줄여야한다. (양수라면 큰 거를)
이게 가능한 이유는 어차피 음수 중에 가장 큰 애를 한 거기 때문에,
더 큰 음수쪽으로 가면 무조건 이득일 수 밖에 없다.
"""

import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

p1 = 0
p2 = N-1
ans = 2000000000 # min
ans1 = 0
ans2 = 0

while p1 < p2:
    cur = solution[p1] + solution[p2]
    if ans > abs(cur):
        ans = abs(cur)
        ans1 = solution[p1]
        ans2 = solution[p2]
    if cur < 0:
        p1 += 1
    elif cur > 0:
        p2 -= 1
    else:
        break

print(ans1, ans2)
