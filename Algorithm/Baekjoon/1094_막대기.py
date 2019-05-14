"""
1094 BOJ 막대기

2019.05.14 PBY
"""

num = 64

X = int(input())

count = 0

while X > 0:
    if num <= X:
        X -= num
        count += 1 # 막대를 합할 때만 빼줘야한다
    else:
        num //= 2
print(count)
