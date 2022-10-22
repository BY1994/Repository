"""
2721 삼각수의 합

수의 합

k*T(k+1) 부분을 처음에 꼼꼼히 보지 않아서 놓침
W(n) 을 호출했을 때 내부에서 T(k+1) 이 있음
"""

import sys
input = sys.stdin.readline

sum_table = [0]*301
t_number = 1
for i in range(1, 301):
    t_number += i + 1
    sum_table[i] = sum_table[i-1] + t_number * i

for T in range(int(input())):
    print(sum_table[int(input())])
