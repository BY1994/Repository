"""
2309 일곱 난쟁이
"""

def dfs(cur, depth, s):
    global flag
    if flag == 1:
        return
    if depth == 7:
        if s == 100:
            flag = 1
            print(*ans, sep='\n')
        return
    for i in range(9):
        if visited[i] == 0:
            visited[i] = 1
            ans[depth] = d[i]
            dfs(i, depth+1, s + d[i])
            visited[i] = 0

flag = 0
d = [0] * 9
visited = [0] * 9
ans = [0] * 7
for i in range(9):
    d[i] = int(input())

d.sort()

for i in range(9):
    visited[i] = 1
    ans[0] = d[i]
    dfs(i, 1, d[i])


"""
9 개 중에 2개 빼는 거니까 for 문 돌면서 2개만 찾으면 되는 거였음
https://www.acmicpc.net/source/2919007
l=[];exec(9*'l+=[int(input())];');l.sort()
for i in l:
	for j in l:
		if i+j==sum(l)-100:l.remove(i);l.remove(j)
for i in l:print(i)

"""
