"""
7568 덩치
"""

N = int(input())
ans = [1] * N
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == j: continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ans[i] += 1

print(*ans, sep=" ")
