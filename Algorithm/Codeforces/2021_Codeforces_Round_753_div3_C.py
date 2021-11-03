"""
Codeforce 753 C

sort 한 후에 diff가 제일 큰 값???
"""

for t in range(int(input())):
    n = input()
    a = list(map(int, input().split()))

    m = -(10**9+1)
    cum = 0
    cur = 0

    a.sort()
    for i in a:
        cur = i - cum
        if cur > m:
            m = cur
        cum += cur

    print(m)
