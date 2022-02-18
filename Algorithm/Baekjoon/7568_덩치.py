"""
7568 덩치

반례
1등이 아닌데 1등이라고 잘못 나옴 -> 수정 완료
두번째 값도 고려가 필요하다

8
5 11
5 12
5 13
6 14
11 5
12 5
13 5
14 6

정답: 2 2 2 1 2 2 2 1
https://www.acmicpc.net/board/view/83188
"""

import sys
input = sys.stdin.readline

origin = []
n = int(input())
for person in range(n):
    weight, height = map(int, input().split())
    origin.append([weight, height])

for person in range(n):
    cnt = 0
    for i in range(n):
        if origin[i][0] > origin[person][0] \
            and origin[i][1] > origin[person][1]:
            cnt += 1
    print(cnt+1, end=" ")

# Wrong Answer
"""
import sys
input = sys.stdin.readline

origin = []
data = []
n = int(input())
for person in range(n):
    weight, height = map(int, input().split())
    origin.append([weight, height])
    data.append([weight, height])

data.sort(reverse = True)

for person in range(n):
    for i in range(n):
        if data[i][0] <= origin[person][0] \
            or data[i][1] <= origin[person][1]:
            print(i+1, end=" ")
            break
"""
