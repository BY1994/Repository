"""
9267 A+B

2019.04.12 PBY 최초작성

1 2 3
YES
3 4 5
NO
3 4 17
YES
"""

a, b, s = map(int, input().split())
possible = 0
q = [[a, b]]
lenq = 1
while q:
    for i in range(lenq):
        nexta, nextb = q.pop(0)
        
        if nexta == s or nextb == s:
            possible = 1
            q = []
            break
        if nexta > s and nextb > s: # 이건 재귀 가지치기가 아님... 불가능한 큐를 끝내야함
            q = []
            break
        q.append([nexta+nextb, nextb])
        q.append([nexta, nextb+nexta])
    lenq = len(q)

print("YES") if possible else print("NO")


# 런타임 에러 => 재귀가 죽은 듯
"""
a, b, s = map(int, input().split())
possible = 0

def operMemory(a, b, s):
    global possible
    if a == s or b == s:
        possible = 1
        return
    if a > s or b > s: # 커져버리면 합으로 원하는 값을 구할 수 없다
        return

    operMemory(a+b, b, s)
    operMemory(a, b+a, s)

operMemory(a, b, s)

print("YES") if possible else print("NO")
"""
