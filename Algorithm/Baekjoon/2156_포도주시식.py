"""
2156 포도주 시식

연속으로 3잔 못 마심!
마지막 잔을 마시는게 이득일 수도 있고, 아닐 수도 있음
max(max(DP[n-1]), max(DP[n-2])) 하고 싶지만
n 이 1이 들어올 수도 있으니, 다음 값을 활용
=> 반례보니까 마지막 잔뿐만 아니라 그 전 잔도 안 마시는게 이득일 수도...

반례
https://raejoonee.tistory.com/15
6 1000 1000 1 1 1000 1000 (두 잔 연속 안 마시는 경우)	4000
"""

n = int(input())
glass = [0] * (n+2)
for i in range(n):
    glass[i] = int(input())

DP = [[0, 0] for i in range(n+2)]
DP[0][0] = glass[0]
DP[1][0] = glass[1]
DP[1][1] = glass[1] + glass[0]
DP[2][0] = glass[2] + glass[0]

for i in range(1,n-1):
    DP[i+1][1] += glass[i+1] + DP[i][0]
    DP[i+2][0] += glass[i+2] + max(max(DP[i][0], DP[i][1]), max(DP[i-1][0], DP[i-1][1]))

print(max(max(DP[n-1]),DP[n][0]))

# 1등 정답
# https://www.acmicpc.net/source/14209584
"""
import sys
I=sys.stdin.readline
a=[int(I())for i in range(int(I()))]
d=[0,a[0],0]
for i in a[1:]:
    d=[max(d),d[0]+i,d[1]+i]  
print(max(d))
"""

# 연속으로 3잔 가능하다고 착각한 풀이
"""
n = int(input())
glass = [0] * (n+2)
for i in range(n):
    glass[i] = int(input())

DP = [[0, 0, 0] for i in range(n+2)]
DP[0][0] = glass[0]
DP[1][0] = glass[1]
DP[1][1] = glass[1] + glass[0]
DP[2][0] = glass[2] + glass[0]

for i in range(1,n-1):
    DP[i+1][1] += glass[i+1] + DP[i][0]
    DP[i+1][2] += glass[i+1] + DP[i][1]
    DP[i+2][0] += glass[i+2] + max(DP[i][0], DP[i][1], DP[i][2])

print(max(DP[n-1]))
"""
