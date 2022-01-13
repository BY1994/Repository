"""
6124 Good Grass
"""

space = []
R, C = map(int, input().split())
for _ in range(R):
    space.append(list(map(int, input().split())))

r, c = 0, 0
ans = 0

for i in range(R-2):
    for j in range(C-2):
        temp = 0
        for x in range(3):
            for y in range(3):
                temp += space[i+x][j+y]
        if temp > ans:
            ans = temp
            r = i+1
            c = j+1

print(ans)
print(r, c)
