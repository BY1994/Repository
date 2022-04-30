"""
4 Chain Reactions
"""

def recur(cur, cur_max, total_cost):
    # next 가면서 max 값들을 가져와서 다 합하고 나까지 더해서 다음에 보냄
    # 자식이 하나면 max 를 올리고
    if count[cur] == 0:
        return F[cur-1]

    if count[cur] == 1:
        return max(cost, recur(edge[cur][0]))

    # 자식이 여럿이면 min 빼고 나머지 합
    
    for c in range(
    
    return cost

DP = [0 for i in range(100001)]
visited = [0 for i in range(100001)]

for tc in range(1, int(input())+1):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))


    # edge
    
    for i in range(N):
        DP[i] = 0

    # i 지점 갔을 때 최대값

    
    # 가리키는 애들을 반대 방향으로 리스트에 넣기
    edge = []
    count = []

    # point 0 인 애들 우선순위 큐에 넣기
    for start in range(N):
        h = []
        if P[start] == 0:
            for c in range(count[start]):
                heapq.heappush(h, (F[start], edge[start][c]))
            visited[start] = tc

            while h:
                cost, node = heapq.heappop(h)
                visited[node] = tc

                for c in range(count[node]):
                    if visited[edge[node][c]] == tc: continue
                    heapq.heappush(h, cost+F[node], edge[node][c])

    print(f"Case #{tc}: {recur(0, 0, 0)}")

"""
visited = [0 for i in range(100001)]

for tc in range(1, int(input())+1):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))

    # 가리키는 애들을 반대 방향으로 리스트에 넣기
    edge = []
    count = []

    # point 0 인 애들 우선순위 큐에 넣기
    for start in range(N):
        h = []
        if P[start] == 0:
            for c in range(count[start]):
                heapq.heappush(h, (F[start], edge[start][c]))
            visited[start] = tc

            while h:
                cost, node = heapq.heappop(h)
                visited[node] = tc

                for c in range(count[node]):
                    if visited[edge[node][c]] == tc: continue
                    heapq.heappush(h, cost+F[node], edge[node][c])

    print(f"Case #{tc}: {}")
"""
