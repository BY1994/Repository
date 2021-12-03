"""
1759 암호 만들기

모음, 자음 개수 조건이 있는데,
문제 읽을 때 놓침
"""

def check(s):
    if s in ['a','e','i','o','u']:
        return True
    return False

def dfs(cur, depth):
    global L, C, mo, ja
    # return 조건이 반드시 있어야하는데 가끔 이 부분을 실수함
    # if 문을 자꾸 합치려고 하는 버릇이 있음
    if depth >= L:
        if mo >= 1 and ja >= 2:
            print(*ans, sep="")
        return
    for i in range(cur+1, C):
        ans[depth] = string[i]
        if check(string[i]) == True:
            mo += 1
            dfs(i, depth+1)
            mo -= 1
        else:
            ja += 1
            dfs(i, depth+1)
            ja -= 1

L, C = map(int, input().split())
string = input().split()
ans = [0] * L
mo = 0
ja = 0
string.sort()

for i in range(C-L+1):
    ans[0] = string[i]
    if check(string[i]) == True:
        mo += 1
        dfs(i, 1)
        mo -= 1
    else:
        ja += 1
        dfs(i, 1)
        ja -= 1
