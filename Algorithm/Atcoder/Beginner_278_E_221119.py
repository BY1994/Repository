# TLE => AC
# 오버랩되는 영역 두 번 계산 안 하게 했더니 통과

H, W, N, h, w = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

count = [0] * 301

cur = 0

for i in range(H):
    for j in range(W):
        count[A[i][j]] += 1
        if count[A[i][j]] == 1:
            cur += 1

previ, prevj = -1, -1
for i in range(H-h+1):
    j = 0
    # 가장 맨 왼쪽은 따로 해주기
    if previ >= 0:
        for i2 in range(previ, previ+h):
            for j2 in range(prevj, prevj+w):
                count[A[i2][j2]] += 1
                if count[A[i2][j2]] == 1:
                    cur += 1

    for i2 in range(i, i+h):
        for j2 in range(j, j+w):
            count[A[i2][j2]] -= 1
            if count[A[i2][j2]] == 0:
                cur -= 1

    print(cur, end=" ")
    previ = i
    prevj = 0

    for j in range(1, W-w+1):
        # 이전 영역 빼고
        # 다음 영역 넣고
        for i2 in range(previ, previ+h):
            j2 = prevj
            count[A[i2][j2]] += 1
            if count[A[i2][j2]] == 1:
                cur += 1
        for i2 in range(i, i+h):
            j2 = j + w - 1
            count[A[i2][j2]] -= 1
            if count[A[i2][j2]] == 0:
                cur -= 1
        previ = i
        prevj = j

        print(cur, end=" ")
    print()
        # 가려지면서 0이 되면 unique 에서 빼고
        # 추가되면서 1이 되면 unique 에 넣기

"""
H, W, N, h, w = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

count = [0] * 301

cur = 0

for i in range(H):
    for j in range(W):
        count[A[i][j]] += 1
        if count[A[i][j]] == 1:
            cur += 1

previ, prevj = -1, -1
for i in range(H-h+1):
    for j in range(W-w+1):
        # 이전 영역 빼고
        # 다음 영역 넣고
        if previ >= 0:
            for i2 in range(previ, previ+h):
                for j2 in range(prevj, prevj+w):
                    count[A[i2][j2]] += 1
                    if count[A[i2][j2]] == 1:
                        cur += 1
        for i2 in range(i, i+h):
            for j2 in range(j, j+w):
                count[A[i2][j2]] -= 1
                if count[A[i2][j2]] == 0:
                    cur -= 1
        previ = i
        prevj = j

        print(cur, end=" ")
    print()
        # 가려지면서 0이 되면 unique 에서 빼고
        # 추가되면서 1이 되면 unique 에 넣기
"""
