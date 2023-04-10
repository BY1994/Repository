"""
25400 제자리

그리디
모든 카드가 다 제자리여야하기때문에 반드시 1부터 순서대로 존재해야한다.
"""

N = int(input())
A = list(map(int, input().split()))
start = 0
card = 0
for a in A:
    if a == start+1:
        start = a
    else:
        card += 1 # 제거
print(card)
