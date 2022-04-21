"""
10830 행렬 제곱 미제출
"""
def mult(p):
    global N
    if p == 1:
        return

    p2 = p//2
    mult(p2)
    for i in range(N):
        for j in range(N):
            result[1][i][j] = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[1][i][j] += result[0][i][k]*result[0][k][j]
                result[1][i][j] %= 1000

    for i in range(N):
        for j in range(N):
            result[0][i][j] = 0

    if p % 2 == 1:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[0][i][j] += result[1][i][k]*origin[k][j]
                    result[0][i][j] %= 1000
    else:
        for i in range(N):
            for j in range(N):
                result[0][i][j] = result[1][i][j]

N, B = map(int, input().split())
origin = []
for _ in range(N):
    origin.append(list(map(int, input().split())))

# 0 current 1 result
result = [[[0 for i in range(N)] for j in range(N)] for k in range(2)]
for i in range(N):
    for j in range(N):
        result[0][i][j] = origin[i][j]
mult(B)

for i in range(N):
    print(*result[0][i])
