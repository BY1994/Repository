N, M = map(int, input().split())
roads = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)
    roads[B].append(A)

for i in range(1,N+1):
    print(len(roads[i]), end=' ')
    roads[i].sort()
    for city in roads[i]:
        print(city, end=' ')
    print()
