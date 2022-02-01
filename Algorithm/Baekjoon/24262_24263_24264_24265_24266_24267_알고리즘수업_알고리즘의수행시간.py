"""
24262 알고리즘 수업 - 알고리즘의 수행 시간 1
24263 알고리즘 수업 - 알고리즘의 수행 시간 2
24264 알고리즘 수업 - 알고리즘의 수행 시간 3
24267 알고리즘 수업 - 알고리즘의 수행 시간 6
"""

# 24262
""" Text
1
0
"""
# 24263
print(input())
print(1)

# 24264
n = int(input())
print(n*n)
print(2)

# 24265 (not submitted)
n = int(input())
print(n*(n-1)/2)
print(2)
# 2, 3, ..., 7 (7-1)
# 3, 4, 5, ...7 (7-2)
# 4, 5, 6, ...7 (7-3)
# 7 (7-6)


# 24266 (not submitted)
n = int(input())
print(n**3)
print(3)

# 24267
n = int(input())
ans = 0
for i in range(1, n-1):
    ans += i*(n-1-i)
print(ans)
print(3)
# 1 + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5)
# 1 - 2 - 3 4 5 6 7
# 1 - 3 - 4 5 6 7
# 1 - 4 - 5 6 7
# ...
# 5 - 6 - 7
# 조합으로 계산

# 정답
# https://www.acmicpc.net/source/37606239
# n=int(input())
# print(n*(n-1)*(n-2)//6,3)
