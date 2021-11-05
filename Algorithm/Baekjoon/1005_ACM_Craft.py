"""
1005 ACM Craft

위상 정렬 연습 문제 (약간 심화)

# 상위권 점수들은 DP 사용
"""

for t in range(int(input())):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    max_parent = [0] * N
    ans = [0] * N

    for i in range(K):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1

    w = int(input())
    
    q = []

    for i in range(N):
        if indegree[i] == 0:
            q.append([i, time[i]])

    while q:
        cur, t = q.pop(0)
        ans[cur] = t

        for node in graph[cur]:
            indegree[node] -= 1
            if max_parent[node] < t:
                max_parent[node] = t
            if indegree[node] == 0:
                q.append([node, max_parent[node]+time[node]])

    print(ans[w-1])
