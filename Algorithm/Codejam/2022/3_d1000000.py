"""
C d1000000
"""

for tc in range(1, int(input())+1):
    N = int(input())
    dice = list(map(int, input().split()))
    dice.sort()

    start = 0
    end = 0
    cur = 0
    while start <= end and end < N:
        if dice[end] >= cur + 1:
            end += 1
            cur += 1
        else:
            start += 1
            cur -= 1

    print(f"Case #{tc}: {cur}")

# Time Limit
"""
for tc in range(1, int(input())+1):
    N = int(input())
    dice = list(map(int, input().split()))
    dice.sort()

    ans = 0
    for start in range(N):    
        cur = 0
        for ind in range(start, N):
            if dice[ind] < cur+1:
                break
            cur += 1
        ans = max(ans, cur)

    print(f"Case #{tc}: {ans}")
"""
