"""
22885 Reversort
"""

for tc in range(int(input())):
    ans = 0
    N = int(input())
    L = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(i, N):       
            if L[j] == i+1:
                ans += j+1 - i
                L[i:j+1] = L[i:j+1][::-1]
                break
    print(f"Case #{tc+1}: {ans}")
