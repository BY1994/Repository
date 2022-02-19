"""
2751 수 정렬하기 2

틀린 이유: 음수가 들어오는데, 고려 못함
"이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다."
https://www.acmicpc.net/board/view/70369
"""

import sys
input = sys.stdin.readline

count = [0] * 2000002
for _ in range(int(input())):
    count[int(input())+1000000] += 1

for i in range(2000002):
    for j in range(count[i]):
        print(i-1000000)
