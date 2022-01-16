"""
17164 Rainbow Beads

틀렸습니다 => 대소문자 틀림
틀렸습니다 => 끊기면 cur = 0 으로 초기화가 아니라 자기 자신부터니까 1부터여야함
"""

N = int(input())
s = input()

ans = 1
cur = 1

if s[0] == 'V':
    cur = 0

for i in range(1, N):
    if s[i] == 'V':
        cur = 0
    elif s[i] == s[i-1]:
        cur = 1
    else:
        cur += 1

    if cur > ans:
        ans = cur

print(ans)
