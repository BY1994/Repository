""" 
1325 효율적인 해킹
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

최초작성 2019.03.15 PBY
"""

# 큐를 배열로 구현
import sys

N, M = list(map(int, sys.stdin.readline().split()))
please_memory = [[] for _ in range(N)]
please_memory_for_depth = [] #[0] * N

for _ in range(M):
    A, B = list(map(int, sys.stdin.readline().split()))
    #please_memory[A-1][0] += 1 # 진입차수
    please_memory[B-1].append(A-1) # 진출 노드들 추가

maxcomputers = 0
for i in range(N):
    #if please_memory[i][0] == 0: # 진입 차수가 제일 적은 애들만 BFS 구현
    visited = [0] * N
    q = [0] * N
    front = 0
    q[0] = i
    rear = 1
    computers = 1
    visited[i] = 1 # 아차 시작점을 추가 안 함
    
    while front != rear:#len(q) > 0:
        j = q[front]
        front += 1
        # 다음 연결된 거 찾아서
        #for j in list(q): # q 로 하면 deque mutated during iteration 에러 메세지
            #q.pop(0)
        #    q.popleft()
        for k in please_memory[j]:
            if visited[k] == 0:
                visited[k] = 1
                q[rear] = k
                rear += 1
                computers += 1 # 나를 포함해서 몇 대가 더 찾아지는지
    if maxcomputers < computers:
        please_memory_for_depth = [i+1]
        maxcomputers = computers
    elif maxcomputers == computers:
        #maxcomputers = computers
        please_memory_for_depth.append(i+1)
#        please_memory_for_depth[i] = computers # 총 찾아진 대수 넣기

for i in please_memory_for_depth:
#    if please_memory_for_depth[i] == maxcomputers:
    print(i, end=' ')



# 큐를 덱으로 구현
    
from collections import deque

N, M = list(map(int, input().split()))
please_memory = [[0] for _ in range(N)]
please_memory_for_depth = [] #[0] * N

for _ in range(M):
    A, B = list(map(int, input().split()))
    please_memory[A-1][0] += 1 # 진입차수
    please_memory[B-1].append(A-1) # 진출 노드들 추가

maxcomputers = 0
for i in range(N):
    #if please_memory[i][0] == 0: # 진입 차수가 제일 적은 애들만 BFS 구현
    visited = [False] * N
    #q = [i]
    q = deque()
    q.append(i)
    computers = 1
    visited[i] = True # 아차 시작점을 추가 안 함
    while q:#len(q) > 0:
        j = q.popleft()
        # 다음 연결된 거 찾아서
        #for j in list(q): # q 로 하면 deque mutated during iteration 에러 메세지
            #q.pop(0)
        #    q.popleft()
        for k in please_memory[j][1:]:
            if visited[k] == False:
                visited[k] = True
                q.append(k)
                computers += 1 # 나를 포함해서 몇 대가 더 찾아지는지
    if maxcomputers < computers:
        please_memory_for_depth = [i+1]
        maxcomputers = computers
    elif maxcomputers == computers:
        #maxcomputers = computers
        please_memory_for_depth.append(i+1)
#        please_memory_for_depth[i] = computers # 총 찾아진 대수 넣기

for i in please_memory_for_depth:
#    if please_memory_for_depth[i] == maxcomputers:
    print(i, end=' ')

"""
시간초과
q를 만드는데 너무 오래걸리나? => deque로 수정

메모리초과
deque를 list로 다시 변환하는 작업이 필요 없음 => 최단경로 문제가 아님!

틀렸습니다
visited가 필수라는 것을 알고 추가했으나, 시작점을 visited로 잡지 않았다.

틀렸습니다
if please_memory[i][0] == 0: # 진입 차수가 제일 적은 애들만 BFS 구현
이 부분이 문제 -> 순환하는 경우를 생각해야한다.
https://www.acmicpc.net/board/view/6899
=> 맞았습니다!
"""

"""
동훈 선생님 코드
from collections import deque

def bfs(_):
    visited = [False] * (N + 1)
    cnt = 0
    hacking = deque()
    hacking.append(_)
    visited[_] = True
    while hacking:
        temp = hacking.popleft()
        for __ in mat[temp]:
            if visited[__] == False:
                visited[__] = True
                hacking.append(__)
                cnt += 1
    return cnt

N, M = list(map(int,input().split()))
mat=[[] for _ in range(N+1)]
for _ in range(M):
    G,S=list(map(int,input().split()))
    mat[S].append(G)

result=deque()
result_num=0

for _ in range(1,N+1):
    cnt_=bfs(_)
    if result_num<cnt_:
        result_num=cnt_
        while result:
            result.pop()
        result.append(_)

    elif result_num==cnt_:
        result.append(_)

for _ in result:
    print(_,end=' ')
"""
