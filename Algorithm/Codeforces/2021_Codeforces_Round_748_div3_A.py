"""
Codeforces #748
"""

for t in range(int(input())):
    votes = list(map(int, input().split()))
    m = -1
    ind = 0
    for i in range(3):
        if votes[i] > m:
            m = votes[i]
            ind = 0
        elif votes[i] == m:
            ind += 1

    for i in range(3):
        if votes[i] == m:
            print(1 if ind > 0 else 0, end=" ")
        else:
            print(m - votes[i] + 1, end=" ")
    print()
