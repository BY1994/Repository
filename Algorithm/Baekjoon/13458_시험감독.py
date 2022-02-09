import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for i in a:
    i -= b
    if i > 0:
        temp = 1 if i%c else 0
        ans += i // c + temp

ans += n
print(ans)
