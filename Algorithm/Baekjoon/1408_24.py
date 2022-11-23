"""
1408 24

반례
https://www.acmicpc.net/board/view/103232
입력
14:00:00
13:52:30

출력
-1:52:30

정답
23:52:30
"""

start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

start = start[2] + start[1]*60 + start[0]*3600
end = end[2] + end[1]*60 + end[0]*3600

ans = end - start
if end < start:
    ans += 24*3600

print(str(ans//3600).zfill(2), end=':')
ans %= 3600
print(str(ans//60).zfill(2), end=':')
ans %=60
print(str(ans).zfill(2))
