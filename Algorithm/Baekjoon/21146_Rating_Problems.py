"""
21146 Rating Problems
"""

n,k=map(int,input().split())
s=sum(float(input()) for _ in range(k))
print((s+(n-k)*(-3))/n,(s+(n-k)*(3))/n)

# 더 숏코딩... 있었음
# https://www.acmicpc.net/source/54308969
"""
n,k,*a=map(int,open(0).read().split())
s=sum(a)
t=3*(k-n)
print((s+t)/n,(s-t)/n)
"""
