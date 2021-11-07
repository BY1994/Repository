"""
Atcoder 224 D

C++ 해설보니 map 으로 visited 처리했으니 hash 로 봐야할 것 같다.

Python dict 쓰면 hash collision 이 나올 텐데?!
마지막 예제가 답이 안 나온다.

맞은 사람들을 보니 dict는 쓰는데 string 으로 input을 썼다...
그러면 collision 을 피할 수 있을까?
=> 마지막 예제가 틀리는 건 그거 때문은 아니었다...

BFS로 가지치기 없이 풀고 visited 안에 distance 넣어놨다가
마지막에 print 하는 방법도 가능

풀이의 차이점을 찾는 중
https://atcoder.jp/contests/abc224/submissions/26785418
https://atcoder.jp/contests/abc224/submissions/26786330
찾았다 내가 empty를 항상 0이라고 가정하고 있었음

그런데... time limit과 wrong answer에 빠졌다...
q = [] 리스트를 q = deque() 덱으로 바꾸고 나서 time limit은 해결되었다
"""

# 답 찾는 걸 매번 하지 않고 최종으로 출력하게 바꿔보기
# 이게 문제가 되는 걸로 보이지는 않지만 다른 답들과 차이가 보여서 테스트
# (그런데 통과한 답 중에 답 보이자마자 break 넣은 답 봄...!)
# 전혀... 결과가 달라지지 않음....여전히 wrong answer 4개

# 해결!!! empty 를 9개 다 보도록 해서 해결함!!!
from collections import deque

def swap(field, a, b):
    tmp = list(field)
    tmp[a], tmp[b] = tmp[b], tmp[a]
    return "".join(tmp)

M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)


p = list(map(int, input().split()))
c = ["0"] * 9
for i in range(8):
    c[p[i]-1] = str(i+1)

# 여기서 실수 있었음!!!
# empty 를 안 찾았던 거랑, 0~7 까지만 보도록 range를 잘못 설정함
# 맨 끝에 0 이 있는 경우 찾지 못했음....
empty = 0
for i in range(9):
    if c[i] == "0":
        empty = i
# queue
visited = {}
#visited = [0] * (8**8 + 1)
q = deque()

c = ''.join(c)

# check_visited(c)
visited[c] = 0

q.append((empty, 0, c)) # empty, dist, cur pieces status
#print(c)

while q:
    cur, dist, field = q.popleft()
    #print(cur, dist, field)
    
    # empty 바톤 터치
    for e in edge[cur]:
        temp = swap(field, cur, e)
        if temp in visited:
            continue
        visited[temp] = dist+1
        q.append((e, dist+1, temp))

if "123456780" in visited:
    print(visited["123456780"])
else:
    print(-1)
    
# deque 로 변경 (time limit 해결 위해서)
"""
from collections import deque

def check_visited(a, empty):
    ind = 0
    #print("ind")
    for i in range(9):
        #print(ind, end=" ")
        ind <<= 4
        ind += (a[i]+1)
    #print(ind)
    if ind in visited:
        return True
    visited[ind] = 1
    return False

def check(a):
    for i in range(8):
        if a[i] != i:
            return False
    return True

M = int(input())
edge = [[0] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[u-1][0] += 1

    edge[v-1].append(u-1)
    edge[v-1][0] += 1


p = list(map(int, input().split()))
c = [-1] * 9
for i in range(8):
    c[p[i]-1] = i


empty = 0
for i in range(8):
    if c[i] == -1:
        empty = i

# queue
visited = {}

q = deque()

check_visited(c, 0)
q.append([empty, 0, c]) # empty, dist, cur pieces status
#print(c)

while q:
    cur = q.popleft()
    #print("cur", cur)
    
    # ans check
    if check(cur[2]):
        print(cur[1])
        break

    # empty 바톤 터치
    for e in edge[cur[0]][1:]:
        #print("next", e)
        temp = cur[2][:]
        # 새로운 위치의 피스를 뺏어와야함
        temp[cur[0]] = temp[e] # empty
        temp[e] = -1 # empty get p
        # edgs's piece
        if check_visited(temp, e):
            continue
        #print("next", temp)
        q.append([e, cur[1]+1, temp])
    
else:
    print(-1)

"""

# time limit (empty 고려 안 한 거 fix)
"""
#piece 위치로?
def check_visited(a):
    if a in visited:
        return True
    visited[a] = 1
    return False

def swap(field, a, b):
    tmp = list(field)
    tmp[a], tmp[b] = tmp[b], tmp[a]
    return "".join(tmp)

def check(a):
    return a == "123456780"

M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)


p = list(map(int, input().split()))
c = ["0"] * 9
for i in range(8):
    c[p[i]-1] = str(i+1)

empty = 0
for i in range(8):
    if c[i] == "0":
        empty = i
# queue
visited = {}
#visited = [0] * (8**8 + 1)
q = []

c = ''.join(c)

check_visited(c)
q.append((empty, 0, c)) # empty, dist, cur pieces status
#print(c)

while q:
    cur, dist, field = q.pop(0)
    print(cur, dist, field)
    #print("cur", cur)
    
    # ans check
    if check(field):
        print(dist)
        break

    # empty 바톤 터치
    for e in edge[cur]:
        temp = swap(field, cur, e)
        #print(temp)
        #print("next", e)
        # 새로운 위치의 피스를 뺏어와야함
        # edgs's piece
        if temp in visited:
            continue
        visited[temp] = 1
        #print("next", temp)
        q.append((e, dist+1, temp))
    
else:
    print(-1)
"""

# 정답 보고 비슷하게 구현
"""
#piece 위치로?
def check_visited(a, empty):
    ind = "".join(a)
    if ind in visited:
        return True
    visited[ind] = 1
    return False

def check(a):
    for i in range(8):
        if a[i] != str(i+1):
            return False
    return True

M = int(input())
edge = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)


p = list(map(int, input().split()))
c = ["0"] * 9
for i in range(8):
    c[p[i]-1] = str(i+1)

# queue
visited = {}
#visited = [0] * (8**8 + 1)
q = []

check_visited(c, 0)
q.append([0, 0, c]) # empty, dist, cur pieces status
#print(c)

while q:
    cur = q.pop(0)
    #print("cur", cur)
    
    # ans check
    if check(cur[2]):
        print(cur[1])
        break

    # empty 바톤 터치
    for e in edge[cur[0]]:
        #print("next", e)
        temp = cur[2][:]
        # 새로운 위치의 피스를 뺏어와야함
        temp[cur[0]] = temp[e] # empty
        temp[e] = "0" # empty get p
        # edgs's piece
        if check_visited(temp, e):
            continue
        #print("next", temp)
        q.append([e, cur[1]+1, temp])
    
else:
    print(-1)
"""

"""
#piece 위치로?
def check_visited(a, empty):
    ind = 0
    #print("ind")
    for i in range(9):
        #print(ind, end=" ")
#        if i == empty: continue
        ind <<= 4
        ind += (a[i]+1)
    #print(ind)
    #if visited.get(ind, 0) == 1:
    if ind in visited:
        return True
    visited[ind] = 1
    return False

def check(a):
    for i in range(8):
        if a[i] != i:
            return False
    return True

M = int(input())
edge = [[0] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[u-1][0] += 1

    edge[v-1].append(u-1)
    edge[v-1][0] += 1


p = list(map(int, input().split()))
c = [-1] * 9
for i in range(8):
    c[p[i]-1] = i

# queue
visited = {}
#visited = [0] * (8**8 + 1)

q = []

check_visited(c, 0)
q.append([0, 0, c]) # empty, dist, cur pieces status
print(c)

while q:
    cur = q.pop(0)
    print("cur", cur)
    
    # ans check
    if check(cur[2]):
        print(cur[1])
        break

    # empty 바톤 터치
    for e in edge[cur[0]][1:]:
        print("next", e)
        temp = cur[2][:]
        # 새로운 위치의 피스를 뺏어와야함
        temp[cur[0]] = temp[e] # empty
        temp[e] = -1 # empty get p
        # edgs's piece
        if check_visited(temp, e):
            continue
        print("next", temp)
        q.append([e, cur[1]+1, temp])
    
else:
    print(-1)

"""
