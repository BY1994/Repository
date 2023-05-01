"""
4966 Cards

두 카드의 최대공약수가 1보다 커야지 매칭 가능
그것만 사전에 처리해두면 기본 이분매칭
append 대신 expend 를 써야하는데,
핸드폰으로 수정해서 제출하느라 그 부분을 생각하지 못했다.
"""

import sys
sys.setrecursionlimit(10**6)

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def dfs(cur):
    global request, result, visited
    for i in request[cur]:
        if visited[i]: continue
        visited[i] = 1
        if result[i] == 0 or dfs(result[i]-1):
            result[i] = cur+1
            return True
    return False

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0: break
    request = [[] for i in range(m)]
    visited = [0]*n
    result = [0]*n
    if m % 10:
        b = list(map(int, input().split()))
    else:
        b = []
    for i in range(m//10):
        b.extend(list(map(int, input().split())))

    if n % 10:
        r = list(map(int, input().split()))
    else:
        r = []
    for i in range(n//10):
        r.extend(list(map(int, input().split())))

    for i in range(m):
        for j in range(n):
            if gcd(b[i],r[j]) > 1:
                request[i].append(j)

    ans = 0
    for i in range(m):
        for j in range(n):
            visited[j] = 0
        if dfs(i):
            ans += 1
    print(ans)
