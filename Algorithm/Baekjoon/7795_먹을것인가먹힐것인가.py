for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    p1 = N-1
    p2 = M-1

    while(p1 >= 0):
        while (p2 >= 0):
            if A[p1] <= B[p2]:
                p2 -= 1
            else:
                break
        ans += p2+1
        p1 -= 1
        
    print(ans)
