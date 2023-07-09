"""
28062 준석이의 사탕 사기

그리디
"""

N = int(input())
candy = list(map(int, input().split()))
candy.sort(reverse=True)
count = 0
ans = 0
last = -1
for c in candy:
    if c % 2:
        count += 1
        last = c
    ans += c
if count % 2 and last != -1:
    ans -= last
print(ans)
