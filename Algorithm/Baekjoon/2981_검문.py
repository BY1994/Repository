"""
2981 검문

정수론, 유클리드 호제법

약수를 구할 때 루트까지만 구해도 되는데,
전체를 다 구해서 시간이 오래 걸렸는지...
=> python3 와 pypy3 의 차이였음
=> python3 로 내려면 sys.stdin.readline 해야함

2022.04.11 시간초과
2022.06.05 통과
"""

# pypy3 로 내서 시간 초과 안 남
def gcd(a, b):
    return gcd(b, a%b) if b else a

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

g = abs(num[0]-num[1])
for i in range(N):
    for j in range(i+1, N):
        g = gcd(g, abs(num[i]-num[j]))

for i in range(2, g+1):
    if g % i == 0:
        print(i, end=" ")
print()


# 틀렸습니다 => i*i > g 에서 break 할 거면 나머지 약수에 대한 출력도 챙겨줬어야함
"""
def gcd(a, b):
    return gcd(b, a%b) if b else a

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

g = abs(num[0]-num[1])

for i in range(1,N-1):
    g = gcd(g, abs(num[i]-num[i+1]))

for i in range(2, g+1):
    if i*i > g:
        break
    if g % i == 0:
        print(i, end=" ")
print(g)
"""

# 시간 초과
"""
def gcd(a, b):
    return gcd(b, a%b) if b else a

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

g = abs(num[0]-num[1])

for i in range(1,N-1):
    g = gcd(g, abs(num[i]-num[i+1]))

# print(g)
for i in range(2, g+1):
    if g % i == 0:
        print(i, end=" ")
print()
"""
