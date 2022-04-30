"""
1202 보석도둑

냅색 문제처럼 보였지만,
가방에 최대 1개만 담을 수 있어서 냅색 문제가 아니었음

그리디라고 분류가 되어있어서 단순 정렬로 풀려고 했지만
그렇게 간단하게 처리되지 않았음..

결국 해답을 확인
https://jaimemin.tistory.com/760
알고리즘은 아래와 같습니다.
1. pair<int, int>형 배열에 보석의 정보를 입력받고 int형 배열에 가방의 정보를 입력받습니다.
2. 보석은 무게를 기준으로 오름차순 정렬을 하고 가방은 최대 무게 허용량을 기준으로 오름차순 정렬을 합니다.
3. 핵심은 한 번 확인한 보석은 다시 확인하지 않는 것입니다.
i) 가방의 개수만큼 반복문을 돌립니다.
ii) 해당 가방이 허용할 수 있는 보석까지 우선순위 큐에 넣습니다.
iii) 우선순위 큐는 maxHeap이기 때문에 넣은 보석들 중 제일 비싼 보석이 root에 있습니다.
iv) 따라서, 우선순위 큐의 root에 있는 보석을 가방에 넣어주고 해당 보석을 우선순위 큐에서 pop합니다.
4. 3번을 모든 가방에 대해 반복합니다.

내림차순으로 하면 안 되는 건가?
생각해봤는데, 가장 무거운 무게의 가방부터 우선순위 큐를 따진다고 생각하면
모든 보석을 다 우선순위큐에 넣어버리게 되는 경우도 있을 수 있음
작은 거부터 제한을 두고 넣는 게 맞을 듯

반례
https://www.acmicpc.net/board/view/73959
2 2
5 5
5 5
1
10
답 5
"""

# 다른 파이썬 답안
# https://www.acmicpc.net/source/40209945
# 1. 왜 bags 넣을 때 min 을 했는지?
# 2. jewelry 인덱스 왜 n 체크를 안 했는지? -> 엣지케이스가 없어서인지

# 시간초과
# readline 쓰고 pypy3 제출해서 통과
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = []
for i in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

bags = []
for i in range(K):
    C = int(input())
    bags.append(C)

jewelry.sort(key = lambda x:(x[0])) # 무게 기준 정렬
bags.sort() # 무게 기준 정렬

ans = 0
h = []
j = 0
for i in range(K):
    while j < N and jewelry[j][0] <= bags[i]:
        heapq.heappush(h, -jewelry[j][1])
        j += 1
    if h:
        ans += -heapq.heappop(h)

print(ans)

# 인덱스 에러 -> if h 추가해줌. 가방에 넣을 수 있는 게 없는 경우 고려
# 틀렸습니다 => heap 에 가치 기준으로 정렬되게 해야함...
"""
import heapq

N, K = map(int, input().split())
jewelry = []
for i in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

bags = []
for i in range(K):
    C = int(input())
    bags.append(C)

jewelry.sort(key = lambda x:(x[0])) # 무게 기준 정렬
bags.sort() # 무게 기준 정렬

ans = 0
h = []
j = 0
for i in range(K):
    while j < N and jewelry[j][0] <= bags[i]:
        heapq.heappush(h, jewelry[j])
        j += 1
    if h:
        ans += heapq.heappop(h)[1]

print(ans)
"""
# 틀렸습니다
# 가격 기준으로 정렬되어 있는데 무게 기준으로는 가능한 애가 지나간 위치에 있을 수 있음
"""
N, K = map(int, input().split())
jewelry = []
for i in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

bags = []
for i in range(K):
    C = int(input())
    bags.append(C)

jewelry.sort(reverse = True, key = lambda x:(x[1], x[0]))
bags.sort(reverse = True)

bind = 0
ans = 0
for i in range(N):
    if bind < K and jewelry[i][0] <= bags[bind]: # bind 가 K 를 넘어가는 경우가 없다고 생각하고 조건 안 넣어서 예제 2 틀림 
        bind += 1
        ans += jewelry[i][1]

print(ans)
"""
