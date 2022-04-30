"""
B 3D Printing
"""

for tc in range(1, int(input())+1):
    C1, M1, Y1, K1 = map(int, input().split())
    C2, M2, Y2, K2 = map(int, input().split())
    C3, M3, Y3, K3 = map(int, input().split())

    c = min(C1, C2, C3)
    m = min(M1, M2, M3)
    y = min(Y1, Y2, Y3)
    k = min(K1, K2, K3)

    if c+m+y+k < 10**6:
        print(f"Case #{tc}: IMPOSSIBLE")
    else:
        ans = 10**6
        print(f"Case #{tc}: ", end="")
        ans -= c
        print(f"{c} ", end="")
        ans -= m
        if ans > 0:
            print(f"{m} ", end="")
        else:
            print(f"{ans+m} ", end="")
            ans = 0
        ans -= y
        if ans > 0:
            print(f"{y} ", end="")
        else:
            print(f"{ans+y} ", end="")
            ans = 0
        ans -= k
        if ans > 0:
            print(f"{k}")
        else:
            print(f"{ans+k}")
            ans = 0
        
