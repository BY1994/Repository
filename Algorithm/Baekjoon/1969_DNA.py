"""
1969 DNA
"""

N, M = map(int, input().split())
DNAs = []
Hdist = 0
ans = ''

for _ in range(N):
    DNAs.append(input())

for i in range(M):
    freq = [0] * 4
    ind = 0
    for j in range(N):
        if DNAs[j][i] == 'A':
            freq[0] += 1
        elif DNAs[j][i] == 'C':
            freq[1] += 1
        elif DNAs[j][i] == 'G':
            freq[2] += 1
        elif DNAs[j][i] == 'T':
            freq[3] += 1

    ans += 'ACGT'[freq.index(max(freq))]

print(ans)

for i in range(N):
    for j in range(M):
        if ans[j] != DNAs[i][j]:
            Hdist += 1
print(Hdist)
        


# 너무... 오래 걸려....
"""
def check(string):
    ret = 0
    for i in range(N):
        for j in range(M):
            if string[j] != DNAs[i][j]:
                ret += 1
    return ret

def dfs(depth, string):
    global M, Hdist, ans
    if depth >= M:
        ret = check(string)
        if ret < Hdist:
            ans = string
            Hdist = ret
        return

    for i in 'ACGT':
        dfs(depth+1, string+i)

N, M = map(int, input().split())
DNAs = []
Hdist = 50000
ans = ''

for _ in range(N):
    DNAs.append(input())

for i in 'ACGT':
    dfs(1, i)


print(ans)
print(Hdist)
"""


# 이렇게 딕셔너리를 쓰면 되는 걸! 내 제출 코드 if elif 부분 고치면 더 보기 좋을 듯
# https://www.acmicpc.net/source/20044464
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
ans = ""
r = n * m
for i in range(m):
    d = dict()
    d["A"], d["T"], d["G"], d["C"] = 0, 0, 0, 0
    for j in range(n):
        d[arr[j][i]] += 1
    m = 0
    temp = ""
    for e in d:
        if m < d[e]:
            m = d[e]
            temp = e
        elif m == d[e]:
            if temp > e:
                temp = e
    r -= d[temp]
    ans += temp
print(ans)
print(r)
"""
