"""
15565_귀여운 라이언

투 포인터
"""
N, K = map(int, input().split())
dolls = list(map(int, input().split()))
count = 0
ryan = []
for i in range(N):
    if dolls[i] == 1:
        ryan.append(i)
        count += 1

ans = N+1
if count > 0:
    cur = 1
p1 = 0
p2 = 0

while p1 < count and p2 < count and p1 <= p2:
    if cur < K:
        p2 += 1
        cur += 1
    else:
        ans = min(ans, ryan[p2] - ryan[p1] + 1)
        p1 += 1
        cur -= 1

if ans == N+1:
    print(-1)
else:
    print(ans)
