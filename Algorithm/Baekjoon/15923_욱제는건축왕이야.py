"""
15923 욱제는 건축왕이야
"""

N = int(input())
starta, startb = map(int, input().split())
preva, prevb = starta, startb
ans = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    if preva == a:
        ans += abs(b - prevb)
    else:
        ans += abs(a - preva)
    preva, prevb = a, b

if preva == starta:
    ans += abs(prevb - startb)
else:
    ans += abs(preva - starta)

print(ans)

# max, min 값만 알면 바로 계산 가능!
# 어차피 둘레를 구하는 것이기 때문에
# https://www.acmicpc.net/source/16366228
"""
x=[];y=[]
for i in range(int(input())):a,b=map(int,input().split());x+=[a];y+=[b]
print(2*(max(x)-min(x)+max(y)-min(y)))
"""
