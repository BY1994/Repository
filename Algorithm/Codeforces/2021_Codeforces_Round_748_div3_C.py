"""
Codeforces #748
"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    mice = list(map(int, input().split()))
    mice.sort()
    cat = 0
    safe = 0

    for i in range(k-1, -1, -1):
        if cat >= mice[i]:
            break
        else:
            cat += n - mice[i]
            safe += 1

    print(safe)
