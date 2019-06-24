"""
1003 피보나치 함수

2019.06.24 PBY 최초작성
"""

fibo = [0]*42
fibo[0] = 1; fibo[1] = 0
for i in range(2, 42):
    fibo[i] = fibo[i-1] + fibo[i-2]

T = int(input())
for test in range(T):
    N = int(input())
    print(fibo[N], fibo[N+1])
