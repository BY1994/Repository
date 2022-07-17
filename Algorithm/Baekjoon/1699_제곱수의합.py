"""
1699 제곱수의 합

100000 쳐보면 시간초과
pypy3 로 제출하고 통과

  0 1 2 3 4 5 6 7 8 9
1 0 1 2 3 4 5 6 7 8 9
2 0       1 2 3 4 2 3
3 0                 1
이렇게 제곱수의 배수마다 다시 최솟값이 갱신됨
이걸 DP 배열에서 min 으로 구하도록 코드를 짬
"""

import math

N = int(input())
DP = [100000]*(N+1)
sqrtN = int(math.sqrt(N))
DP[0] = 0

for i in range(1, sqrtN+1):
    num = i*i
    for j in range(1, N+1):
        DP[j] = min(DP[j % num]+(j // num), DP[j])

print(DP[N])

# 시간초과
"""
import math

N = int(input())
DP = [100000]*(N+1)
sqrtN = int(math.sqrt(N))
DP[0] = 0

for i in range(1, sqrtN+1):
    num = i*i
    for j in range(1, N+1):
        if num*j > N:
            break
        for k in range(num*j, num*(j+1)):
            if k > N:
                break
            DP[k] = min(DP[k-num]+1, DP[k])
            
print(DP[N])
"""
