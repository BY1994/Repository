n, k, a = map(int, input().split())
ans = ((k % n) + (a - 1))%n
if ans:
    print(ans)
else:
    print(n)


# 5 4 1 이랑 5 4 2가 다 4가 나옴
"""
n, k, a = map(int, input().split())
if n > k:
    print(k)
else:
    ans = ((k % n) + (a - 1))%n
    if ans:
        print(ans)
    else:
        print(n)
"""

# 4 15 3 하니까 또 5나옴....
"""
n, k, a = map(int, input().split())
if n > k:
    print(k)
else:
    ans = (k % n) + (a - 1)
    if ans:
        print(ans)
    else:
        print(n)
"""

# 4 14 1 넣으니까 사람이 4명인데 5가 나와....
"""
n, k, a = map(int, input().split())
if n > k:
    print(k)
else:
    ans = (k % n) + (n - a)
    if ans:
        print(ans)
    else:
        print(n)
"""
