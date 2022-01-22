"""
15813 너의 이름은 몇 점이니?

단순 합
"""

N = int(input())
ans = 0
basis = ord('A')-1
for alpha in input():
    ans += ord(alpha) - basis
print(ans)


# 속도 1등 정답
# https://www.acmicpc.net/source/10249168
# a=input;a();print(sum(ord(x)-64 for x in a()))
