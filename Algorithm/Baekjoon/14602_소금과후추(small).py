picture = []
M, N, K, W = map(int, input().split())
for _ in range(M):
    picture.append(list(map(int, input().split())))

w = [0] * (W*W)
B = [[] for _ in range(M-W+1)]
middle = (W*W)//2
for i in range(M-W+1):
    for j in range(N-W+1):
        ind = 0
        for x in range(W):
            for y in range(W):
                w[ind]= picture[i+x][j+y]
                ind += 1
        w.sort()
        B[i].append(w[middle])


for i in range(M-W+1):
    print(*B[i])
