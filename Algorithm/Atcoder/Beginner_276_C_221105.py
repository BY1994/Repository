"""
나보다 작은 수가 내 오른쪽에 있으면 나랑 교환 가능
"""

N = int(input())
P = list(map(int, input().split()))

candidate = set()
flag = 0
pos = -1
for i in range(N-1, -1, -1):
    cur = P[i]
    for j in range(N-1, i, -1):
        if cur > P[j]:
            candidate.add(cur)
            candidate.add(P[j])
            if pos < P[j]:
                pos = P[j]
            flag = 1
#            break
        else:
            candidate.add(P[j])
    if flag == 1:
        candidate = list(candidate)
        candidate.sort(reverse=True)
        print(*P[:i], pos, end = ' ')
        for c in candidate:
            if c == pos:
                continue
            print(c, end=' ')
        print()
        break
