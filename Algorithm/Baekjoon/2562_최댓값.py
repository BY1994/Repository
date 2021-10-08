"""
2562 최댓값
"""

ans = 0
ind = 1
for i in range(9):
    cur = int(input())
    if cur > ans:
        ans = cur
        ind = i + 1
print(ans)
print(ind)

# 숏코딩
"""
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)
"""
