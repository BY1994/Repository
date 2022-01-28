"""
16440 제이크와 케이크

Necklace splitting problem
Borsuk-Ulam theorem
"""

N = int(input())
cake = input()
s = 0
for i in range(N//2):
    if cake[i] == 's':
        s += 1

if s == N//4:
    print(1)
    print(N//2)
else:
    for i in range(N//2):
        if cake[i] == 's':
            s -= 1
        if cake[i+N//2] == 's':
            s += 1
        if s == N//4:
            print(2)
            print(i+1, i+N//2+1)
            break

# 참고
# https://www.acmicpc.net/source/10764861
"""
n = int(input())
h = n//2
cake = [(1 if c == 's' else -1) for c in input()]

s = sum(cake[:h])
if s == 0: print(1); print(h); exit()
for i in range(h, n):
    s+= cake[i] - cake[i-h]
    if s == 0: print(2); print(i-h+1, i+1); break
"""

# 내 틀린 풀이
"""
N = int(input())
s = input()

num1 = 0
num2 = 0
ans = 0
ind = 0

for i in range(N//2):
    if s[i] == 's':
        num1 += 1
    else:
        num2 += 1

if num1 == num2:
    ans = 1
    ind = N//2+1
else:
    ans = 2

for i in range(N//2):
    if s[i] == 's':
        num1 -= 1
    else:
        num2 -= 1

    if s[i+N//2] == 's':
        num1 += 1
    else:
        num2 += 1

    if num1 == num2:
        ind = i+1
        break

print(ans)
if ans == 2:
    print(ind, ind + N//2)
else:
    print(ind)
"""
