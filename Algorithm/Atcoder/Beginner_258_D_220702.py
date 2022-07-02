"""
Atcoder 258 (2022.07.02)

문제를 너무 어렵게 접근했다.
대회가 끝나고 그림을 그려보고 더 쉬운 풀이가 가능할 것 같아서 구현해봤는데, 통과하였다.
최적화된 완전 탐색에 가까운 풀이인 것 같다.
"""

# DP 문제인 것 같아서 냅색으로 풀어보려다 실패
# 아래와 같이 단순하게 구현해도 될 것 같아서 해봤는데 예제가 안 나왔다.
# 문제 해결 => minv 를 업데이트를 맨 밑에서 시켜줘서 제때 반영이 안 되고 있었음
# 틀렸습니다 => ans 를 10의 18 승까지 가능한데, 더 작게 잡아서 틀렸음

N, X = map(int, input().split())
stages = [[0 for i in range(2)] for j in range(N+1)]

for i in range(N):
    A, B = map(int, input().split())
    stages[i][0] = A
    stages[i][1] = B

ans = (10**18)*2
minv = stages[0][1]
basic = 0
for i in range(min(X, N)):
    basic += stages[i][0] + stages[i][1]
    minv = min(minv, stages[i][1])

    temp = basic
    temp += (X-i-1)*minv
    ans = min(ans, temp)

print(ans)

# 잘못된 풀이
# 전체적으로 봤을 때 다음 stage 로 진전하는게 이득인 경우가 고려 안 됨
# 이런 그리디 방식 말고 DP 방식이 필요
"""
import heapq
h = []
N, X = map(int, input().split())
stages = [[0 for i in range(2)] for j in range(N)]
max_visit = 1
ans = 0
times = 0
for i in range(N):
    A, B = map(int, input().split())
    stages[i][0] = A
    stages[i][1] = B

heapq.heappush(h, (stages[0][0] + stages[0][1], 0))

while h:
    time, cur = heapq.heappop(h)
    ans += time
    times += 1
    #print(time, cur, ans, times)
    if times >= X:
        print(ans)
        break
    
    heapq.heappush(h, (stages[cur][1], cur))
    if max_visit-1 == cur and max_visit < N:
        max_visit += 1
        heapq.heappush(h, (stages[cur+1][0] + stages[cur+1][1], cur+1))
"""
