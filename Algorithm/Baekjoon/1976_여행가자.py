"""
1976 여행 가자

유니온 파인드
실수 포인트
1. 맨 마지막에 find(left) != find(right) 라고 적어버림
2. parent[parent[a]] = parent[b] 가 아닌
parent[a] = parent[b] 라고 적었는데 예제가 맞아서 제출했음
하지만 그러면 a의 부모에 연결된 다른 자식들은 최상위 부모가 바뀌었는지 알 수 없음
a 의 부모만 변경됨
"""

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if find(a) != find(b):
        # 상위 부모가 나만의 부모가 아닐 수 있음
        parent[parent[a]] = parent[b]
    return

N = int(input())
M = int(input())
parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i
connection = []
for i in range(N):
    connection = list(map(int, input().split()))
    # i, j 연결이면 union
    for j in range(N):
        if connection[j] == 0:
            continue
        union(i+1, j+1)

schedule = list(map(int, input().split()))
left = 0
for right in range(1, M):
    if find(schedule[left]) != find(schedule[right]):
        print("NO")
        break
    left = right
else:
    print("YES")
