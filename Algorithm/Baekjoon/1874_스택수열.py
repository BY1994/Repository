"""
1874 스택 수열

ans 크기를 잘못 잡아서 런타임 에러
"""

N = int(input())
stack = [0]*100001
#ans = [0]*100001
#ind = 0
#sp = -1
cur = 1
flag = 0

stack[0] = 1
sp = 1
ans = ['+']
#ans[0] = '+'
#ind = 1

for i in range(N):
    num = int(input())

    if flag == 1:
        continue

    while stack[sp-1] < num:
        cur += 1
        stack[sp] = cur
        ans.append('+')
#        ans[ind] = '+'
#        ind += 1
        sp += 1

    while stack[sp-1] > num:
        sp -= 1
        ans.append('-')
#        ans[ind] = '-'
#        ind += 1
        
    if stack[sp-1] != num:
        flag = 1
        continue

    # same
    sp -= 1
    ans.append('-')
#    ans[ind] = '-'
#    ind += 1

if flag == 1:
    print('NO')
else:
    for i in ans:
        print(i)

    #for i in range(ind):
    #    print(ans[i])
