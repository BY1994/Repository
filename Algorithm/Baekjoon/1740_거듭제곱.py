"""
1740 거듭제곱

비트마스킹
"서로 다른" 3의 배수를 합하는 것이므로
이진수처럼 생각해도 됨
"""

N = int(input())
ans = 0
num = 1
while N > 0:
    if (N & 1): ans += num
    num *= 3
    N >>= 1
print(ans)
