"""
18870 좌표 압축
"""

N = int(input())
X = list(map(int, input().split()))

newX = list(zip(X, list(range(N))))

newX.sort(key=lambda x:x[0])

prev = newX[0][0]
ind = 0
ans = []
for x in newX:
    if x[0] != prev:
        ind += 1
    prev = x[0]
    ans.append(ind)

newX = list(zip(newX, ans))
newX.sort(key = lambda x:x[0][1])

for i in range(N):
    print(newX[i][1], end=" ")


# https://www.acmicpc.net/source/28431292
# set으로 만들어서 counting sort 비슷하게 진행된 듯
"""
n = int(input())
x = list(map(int, input().split()))
x2 = list((set(x)))
x2.sort()
x3 = {}
a = 0
for i in x2:
  x3[i] = a
  a += 1
for i in range(n):
  x[i] = x3[x[i]]
print(' '.join(map(str, x)))
"""
