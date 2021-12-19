"""
2503 숫자 야구

반례
https://www.acmicpc.net/board/view/37607

1
123 0 2
오답 66
정답 54

오답 원인
python i 를 str 으로 바꾸니까
다음 for 문에서 
"""

N = int(input())
Q = []
for _ in range(N):
    Q.append(input().split())

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i == j: continue
        for k in range(1, 10):
            # 여기 str 로 들어오니까 비교 에러가 남!!!!
            if i == k or j == k: continue
            #print(i, j, k, i == j, i ==k, j ==k, type(i),type(j), type(k))
            for q in range(N):
                strike = 0
                ball = 0
                #i = str(i)
                #j = str(j)
                #k = str(k)
                a = str(i)
                b = str(j)
                c = str(k)
                if a == Q[q][0][0]:
                    strike += 1
                elif a in Q[q][0]:
                    ball += 1
                if b == Q[q][0][1]:
                    strike += 1
                elif b in Q[q][0]:
                    ball += 1
                if c == Q[q][0][2]:
                    strike += 1
                elif c in Q[q][0]:
                    ball += 1

                if int(Q[q][1]) != strike or int(Q[q][2]) != ball:
                    break
            else:
                #print(i, j, k)
                ans += 1
print(ans)



# https://www.acmicpc.net/source/6651612
"""
def guess(x, real):
    strike = 0
    ball = 0
    for i in range(3):
        if x[i] == real[i]: strike+= 1
        elif x[i] in real: ball+= 1
    return strike, ball

def poss(x, q):
    for real, s, b in q:
        if guess(x, str(real)) != (s, b): return False
    return True

n = int(input())
q = [tuple(map(int,input().split())) for i in range(n)]
res = 0
for i in range(123, 999):
    s = str(i)
    if '0' in s: continue
    if not (s[0] != s[1] != s[2] != s[0]): continue
    if poss(s, q): res+= 1
print(res)
"""

