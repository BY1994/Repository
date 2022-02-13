"""
12784 인하니카 공화국

내가 가지고 있는 값과, 자식들이 합해준 값을 비교

시간초과 => pypy3 로 제출하고 해결

반례
1
1 0
정답 0

틀렸습니다 => 리프 노드만 차단하면 되는 듯

1
3 2
1 2 1
1 3 4
정답 5

풀이를 보니 dfs
https://velog.io/@sunjoo9912/%EB%B0%B1%EC%A4%80-12784-%EC%9D%B8%ED%95%98%EB%8B%88%EC%B9%B4-%EA%B3%B5%ED%99%94%EA%B5%AD

내 풀이 반례 만들기
1
3 2
1 2 2
2 3 1
정답 1
"""

import sys
input = sys.stdin.readline

connect = [[0 for i in range(1000)] for j in range(1000)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(n):
        for j in range(n):
            connect[i][j] = 0
    indegree = [0]*n
    # 식이 준 값
    compare = [0]*n

    # 반례 처리
    if m == 0:
        print(0)
        continue
    
    for __ in range(m):
        a, b, d = map(int, input().split())
        indegree[a-1] += 1
        indegree[b-1] += 1
        connect[a-1][b-1] = d
        connect[b-1][a-1] = d
    
    q = []
    qs = 0
    qe = 0

    # 개수가 1인 애들
    indegree[0] += 1 # 이것만 부모가 없어서 1이 덜 들어감
    for i in range(n):
        if indegree[i] == 1:
            q.append(i)
            qe += 1
            compare[i] = 1000000

    while qs < qe:
        current = q[qs]
        qs += 1
        indegree[current] -= 1

        for i in range(n):
            d = connect[current][i]
            if d > 0:
                connect[i][current] = 0
                indegree[i] -= 1
                # 내 부모에게 내가 가진 값과 연결 값 중 더 작은 걸 줌
                compare[i] += d if d < compare[current] else compare[current]
                if indegree[i] == 1:
                    q.append(i)
                    qe += 1
                break
                
    print(compare[0])

# 틀렸습니다 => 모든 노드를 다 고려하는게 맞다
# 다이너마이트가 상위에서 더 적을 수도 있으니
"""
import sys
input = sys.stdin.readline

connect = [[0 for i in range(1000)] for j in range(1000)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(n):
        for j in range(n):
            connect[i][j] = 0
    indegree = [0]*n
    # 내 값과 자식이 준 값
    compare = [0]*n
    for __ in range(m):
        a, b, d = map(int, input().split())
        indegree[a-1] += 1
        indegree[b-1] += 1
        connect[a-1][b-1] = d
        connect[b-1][a-1] = d
    
    q = []
    qs = 0
    qe = 0
    # 개수가 1인 애들
    for i in range(n):
        if indegree[i] == 1:
            q.append(i)
            qe += 1

    indegree[0] += 1 # 이것만 부모가 없어서 1이 덜 들어감

    q2 = []
    qs2 = 0
    qe2 = 0
    while qs < qe:
        current = q[qs]
        qs += 1
        indegree[current] -= 1
        # 내 부모에게 내가 가진 값과 연결 값 중 더 작은 걸 줌

        for i in range(n):
            d = connect[current][i]
            if d > 0:
                connect[i][current] = 0
                indegree[i] -= 1
                compare[i] += d
                if indegree[i] == 1:
                    q2.append(i)
                    qe2 += 1
                break # 부모는 하나 뿐
    ans = 0
    while qs2 < qe2:
        current = q2[qs2]
        qs2 += 1

        for i in range(n):
            d = connect[current][i]
            if d > 0:
                #print(current, i, d)
                ans += d if d < compare[current] else compare[current]
                break
    # 1 에 바로 연결된 리프 노드는?
    print(ans + compare[0])
"""

# 리프노드만 차단한 게 아니라 모든 노드를 차단
"""
import sys
input = sys.stdin.readline

connect = [[0 for i in range(1000)] for j in range(1000)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(n):
        for j in range(n):
            connect[i][j] = 0
    indegree = [0]*n
    # 내 값과 자식이 준 값
    compare = [0]*n
    for __ in range(m):
        a, b, d = map(int, input().split())
        indegree[a-1] += 1
        indegree[b-1] += 1
        connect[a-1][b-1] = d
        connect[b-1][a-1] = d
    
    q = []
    qs = 0
    qe = 0
    # 개수가 1인 애들
    for i in range(n):
        if indegree[i] == 1:
            q.append(i)
            qe += 1
            compare[i] = 1000000

    indegree[0] += 1 # 이것만 부모가 없어서 1이 덜 들어감


    while qs < qe:
        current = q[qs]
        qs += 1
        indegree[current] -= 1
        # 내 부모에게 내가 가진 값과 연결 값 중 더 작은 걸 줌

        for i in range(n):
            d = connect[current][i]
            if d > 0:
                connect[i][current] = 0
                indegree[i] -= 1
                compare[i] += d if d < compare[current] else compare[current]
                if indegree[i] == 1:
                    q.append(i)
                    qe += 1
                
    print(compare[0])
"""

"""
[[0, 1, 0, 0, 4, 0, 0, 0],
[1, 0, 4, 1, 0, 0, 0, 0],
[0, 4, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[4, 0, 0, 0, 0, 1, 2, 0],
[0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
"""


# DFS 버전 https://www.acmicpc.net/source/36691655
"""
import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    dynamite = 0
    for g in graph[x]:
        if not visited[g[0]]:
            dynamite += min(g[1], dfs(g[0]))
    return dynamite if dynamite else 10000


for _ in range(int(input().rstrip())):
    N, M = map(int, input().rstrip().split())
    if N == 1:
        print(0)
    else:
        graph = [[] for _ in range(N + 1)]
        visited = [False for _ in range(N + 1)]
        for _ in range(M):
            a, b, c = map(int, input().rstrip().split())
            graph[a].append((b, c))
            graph[b].append((a, c))
        print(dfs(1))
"""
