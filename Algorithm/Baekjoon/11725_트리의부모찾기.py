"""
11725 트리의 부모 찾기

그래프 탐색 (DFS, BFS)

트리란 사이클이 없이 "모든 정점이 연결"되어있는 그래프이다.
문제의 본문대로 루트 없는 트리라고 검색해서 나온 게시글인데, 트리는 꼭 루트가 있어야하는 건 아니라고 한다.
모든 정점이 연결되어있다는 점이 중요한 것 같다. (풀이를 작성할 때 하나에서부터 순회를 하면 모든 정점을 결국 다 순회할 수 있으므로)
https://velog.io/@kjh107704/%ED%8A%B8%EB%A6%AC-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EA%B8%B0%EC%B4%88
"""

N = int(input())
edge = [[] for i in range(N+1)]
parents = [-1]*(N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = [1]
qs = 0
qe = 1
while qs < qe:
    parent = q[qs]
    qs += 1

    for next in edge[parent]:
        if parents[next] != -1:
            continue
        parents[next] = parent
        q.append(next)
        qe += 1

for i in range(2, N+1):
    print(parents[i])
