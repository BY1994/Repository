"""
13135 Corrupt Election

값/좌표 압축 문제
해설
https://gooddaytocode.blogspot.com/2016/08/blog-post_6.html

들어온 좌표만 정렬을 해서 좌표 압축이 된다는 것도 몰랐고
문제를 뒤집어서 무효표가 아닌 유효표를 고려하면 된다는 것도 몰랐다
"""

N = int(input())
people = []
ans = 0
x = {0, 100000} # for range
y = {0, 100000}
xind = [0] * 100010
yind = [0] * 100010

for _ in range(N):
    coor = list(map(int, input().split()))
    people.append([max(coor), sum(coor), coor[0] - coor[1]])

    x.add(max(coor))
    y.add(sum(coor))

xc = sorted(list(x))
yc = sorted(list(y))

D = [[0] * len(yc) for _ in range(len(xc))]

for i, v in enumerate(xc):
    xind[v] = i
for j, v in enumerate(yc):
    yind[v] = j

for p in people:
    D[xind[p[0]]][yind[p[1]]] = p[2]

xc_len = len(xc)
yc_len = len(yc)

for i in range(xc_len):
    for j in range(yc_len):
        if i > 0 and j > 0 and i < xc_len-1 and j < yc_len-1:
            D[i][j] += D[i-1][j] + D[i][j-1] - D[i-1][j-1]
            if D[i][j] > 0:
                ans += (xc[i+1]-xc[i]) * (yc[j+1] - yc[j])    
    
print(ans)
