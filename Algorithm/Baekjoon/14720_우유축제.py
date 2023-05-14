"""
14720 우유 축제

그리디
"""

N = int(input())
store = list(map(int, input().split()))
cur = 0
ans = 0
for s in store:
    if cur == s:
        ans += 1
        cur = (cur+1)%3
print(ans)
