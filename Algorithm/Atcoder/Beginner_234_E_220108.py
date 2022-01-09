# 234 E
"""
X = input()
N = int(X)
n = len(X)

start = int(X[0])
diff = int(X[0])-int(X[1])

for i in range(

b = 0
flag = 0
for i in range(2, n):
    curd = int(X[i]) - int(X[i-1])
    if curd > diff:
        b = i-1
        flag = 1
        break
    elif curd < diff:
        b = i-1
        flag = 2
        break
else:
    print(N)

if flag >= 1:
    while True:
        # 지금 내 수에다가 계속 증가시켜 가면서
        
"""

N = input()

if len(N) == 1:
    print(N)
else:
    is_answer = False
    a = int(N[0])
    b = int(N[1])
    diff = 0
    new_val = 0
    while True:
        diff = b-a
        fin_val = a + (len(N)-1)*diff
        if fin_val >= 10 or fin_val < 0:
            is_answer = False
        else:
            new_val = int("".join(map(str, [a+i*diff for i in range(0, len(N))])))
            if new_val >= int(N):
                is_answer = True
                break
        s = str(a*10+b+1)
        a = int(s[0])
        b = int(s[1])

    print(new_val)
