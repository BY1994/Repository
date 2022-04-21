# 1992 쿼드트리

def find(x, y, size):
    first = image[x][y]
    flag = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if first != image[i][j]:
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        print("(", end="")
        nsize = size//2
        find(x, y, nsize)
        find(x, y+nsize, nsize)
        find(x+nsize, y, nsize)
        find(x+nsize, y+nsize, nsize)
        print(")", end="")
    else:
        print(first, end="")

image = []
N = int(input())
for _ in range(N):
    image.append(input())

first = image[0][0]
flag = 0
for i in range(N):
    for j in range(N):
        if first != image[i][j]:
            flag = 1
            break
    if flag == 1:
        break

if flag == 1:
    print("(", end="")
    nsize = N//2
    find(0, 0, nsize)
    find(0, nsize, nsize)
    find(nsize, 0, nsize)
    find(nsize, nsize, nsize)
    print(")")
else:
    print(first)
