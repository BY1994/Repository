"""
2581 소수

반례
1
6
오답 11 1 나옴
정답은 10 2 임
"""

M = int(input())
N = int(input())

check = [0] * (N+1)
check[1] = 1
for i in range(2, N):
    for j in range(2, 10001): # 1 곱하면 자기자신
        if i*j > N:
            break
        check[i*j] = 1

ans = []
for i in range(M, N+1):
    if check[i] == 0:
        ans.append(i)

if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)

# https://www.acmicpc.net/source/10986104
"""
def eratos():
    for i in range(2, 101):
        if table[i]:
            for j in range(i*2, 10001, i):
                table[j] = False
"""
