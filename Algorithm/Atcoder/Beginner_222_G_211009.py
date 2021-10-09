"""
atcoder
#G
"""

# Wrong
T = int(input())

for t in range(T):
    k = int(input())
    ans = 1
    n = 2
    # 10**8 이니까 2가 8번 넘게 나오면 됨
    for i in range(9):
        if n % k == 0:
            print(ans)
            break
        ans += 1
        n *= 10
        n += 2
    else:
        print(-1)
    
