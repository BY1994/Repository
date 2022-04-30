"""
(a + b + c)(a + b + c)
=a**2 + ab + ac + ba + b**2 + bc + ac + bc + c**2
=>
2ab + 2ac + 2bc = 0
a(b+c) = -bc

(a+b+c+d)(a+b+c+d)
= a**2 + ab + ac + ad + ab+ b**2 + bc+bd
+ ac + bc + c**2 + cd + ad + bd + cd + b**2

=>
2ab + 2bc + 2ac + 2ad + 2bd + 2cd = 0
a(b+c+d) + bc+bc+cd = 0

-d(a+b+c) = ab+bc+ac

(a + b + c)**2 = a**2 + b**2 + c**2
"""

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    E = list(map(int, input().split()))

    ans = 0
    sumE = sum(E)

    for i in range(N):
        for j in range(i+1, N):
            ans += E[i]*E[j]

    if sumE != 0: # 예제 3 에러 처리
        ans //= (sumE)

    ans *= -1

    sumE += ans
    left = sumE * sumE
    right = ans*ans
    for i in range(N):
        right += E[i]*E[i]

    if ans > 10**18 or ans < -10**18 or left != right:
        print(f"Case #{tc}: IMPOSSIBLE")
    else:
        print(f"Case #{tc}: {ans}")

# brute force 하려고 했는데 범위가 너무 큼
"""
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    E = list(map(int, input().split()))

    sumE = sum(E)
    left = sumE*sumE
    right = 0
    for i in range(N):
        right += E[i]*E[i]

""" 
