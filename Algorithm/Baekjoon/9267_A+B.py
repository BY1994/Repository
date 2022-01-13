"""
9267 A+B

2019.04.12 PBY 최초작성

1 2 3
YES
3 4 5
NO
3 4 17
YES

만들어지는 과정
3 4 17 
3 7 17 b += a
10 7 17 a += b
17 7 17 a += b


"""
# 확장 유클리드 호제법으로 변경 (2021.10.05)

def xgcd(a, b, S):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while True:
        q = r1 // r2
        r = r1 - (q * r2)
        s = s1 - (q * s2)
        t = t1 - (q * t2)

        #print(r2, s2, t2, q, r, s, t)
        if r == 0 or r == S:
            # gcd: r2, s: s2, t: t2
            return s2, t2 # inverse of multiply

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

a, b, S = map(int, input().split())

x, y = xgcd(a, b, S)
print(x, y)


# 수정하다 제출 안 한 과거 코드
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
"""

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
