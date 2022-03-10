"""
9461 파도반 수열

1 1 2 2 3 4 5 7 9

5 = 1 + 4
7 = 2 + 5
9 = 2 + 7
바로 앞에 숫자와 5번째 전 숫자
"""

P = [0 for i in range(100)]
P[0] = 1
P[1] = 1
P[2] = 1
P[3] = 2
P[4] = 2
for i in range(5, 100):
    P[i] = P[i-1] + P[i-5]

for _ in range(int(input())):
    print(P[int(input())-1])
