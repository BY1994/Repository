"""
2630 색종이 만들기

분할정복
"""

def find(x, y, size):
    global white, blue
    
    first = paper[x][y]
    flag = 0
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if first != paper[i][j]:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        nsize = size // 2
        find(x, y, nsize)
        find(x, y+nsize, nsize)
        find(x+nsize, y, nsize)
        find(x+nsize, y+nsize, nsize)
    else:
        if first == 0:
            white += 1
        else:
            blue += 1

N = int(input())
paper = []

white = 0
blue = 0

for _ in range(N):
    paper.append(list(map(int ,input().split())))

find(0, 0, N)

print(white)
print(blue)
