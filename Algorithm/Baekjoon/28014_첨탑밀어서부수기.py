"""
28014 첨탑 밀어서 부수기

그리디

"클 때만" 뒤에 있는 첨탑이 밀려 넘어가기 때문에
H[i+1] >= H[i] 이렇게 반드시 등호가 필요하다.
등호 없이 제출했다가 틀림
"""

N = int(input())
H = list(map(int, input().split()))
ans = 1
for i in range(N-1):
    if H[i+1] >= H[i]:
        ans += 1
print(ans)
