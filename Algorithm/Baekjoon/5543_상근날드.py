"""
5543 상근날드
"""

b = 3000
d = 3000

for i in range(3):
    val = int(input())
    if b > val: b = val

for i in range(2):
    val = int(input())
    if d > val: d = val

print(b + d - 50)

"""
반례 찾기 연습
https://www.acmicpc.net/board/view/56693

if priceArray[i] < priceArray[i + 1] {
  cheapBugger = priceArray[i]

600
800
700
100
100

하면 650 이 나와야하는데, 750 이 나오는 코드
if문에서 min 값을 비교하지 않고, input 값 끼리 비교하기 때
"""
