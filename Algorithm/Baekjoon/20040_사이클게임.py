"""
20040 사이클 게임

시간초과 해결 방법
find 를 재귀말고 while 문으로 변경
https://www.acmicpc.net/board/view/92706

시간초과 해결 방법
sys.stdin.readline
https://mooyoungblog.tistory.com/37

시간초과 이유
a b 들어오고
b a 들어오면 무한 사이클 생김?
재귀든 while 이든 시간 초과에 갇혀버림
맞나? 무한 사이클이 아닌가? 반례 만들어봤는데 안 생김
=> 찾아보니 시간을 빠르게하기 위한 최적화 방법이라고 한다. (Union by Rank)
https://people.cs.georgetown.edu/jthaler/ANLY550/lec6.pdf
The idea of UNION BY RANK is to ensure that when we combine two trees,
we try to keep the overall depth of the resulting tree small.
그러면 반례로
1000 -> 999 -> 998 -> 997 -> 996 -> 995 ..
이런식으로 연결한 다음에
find(1000) == find(1) 이런 식으로 재귀를 엄청 타게 하면?
"""

# 통과 코드
import sys
input = sys.stdin.readline

def find(x):
    origin = x
    while x != parent[x]:
        x = parent[x]
    parent[origin] = x
    return x

def union(a, b):    
    if find(a) == find(b):
        return
    if parent[a] < parent[b]:
        parent[parent[a]] = parent[b]
    else:
        parent[parent[b]] = parent[a]
    return

n, m = map(int, input().split())
parent = [0] * (n)
for i in range(n):
    parent[i] = i
flag = 0
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if flag == 0 and find(a) == find(b):
        flag = 1
        ans = i+1
    else:
        union(a, b)
print(ans)

# 시간초과
"""
import sys
input = sys.stdin.readline

def find(x):
    origin = x
    while x != parent[x]:
        x = parent[x]
    parent[origin] = x
    return x

def union(a, b):    
    if find(a) == find(b):
        return
    parent[parent[a]] = parent[b]
    return

n, m = map(int, input().split())
parent = [0] * (n)
for i in range(n):
    parent[i] = i
flag = 0
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if flag == 0 and find(a) == find(b):
        flag = 1
        ans = i+1
    else:
        union(a, b)
    print(a, b, parent) # 반례 찾아보려 했지만 무한 싸이클 같은 건 안 생겼다.
print(ans)
"""

# 시간초과
"""
import sys
sys.setrecursionlimit(100000000)

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if find(a) == find(b):
        return
    parent[parent[a]] = parent[b]
    return

n, m = map(int, input().split())
parent = [0] * (n)
for i in range(n):
    parent[i] = i
flag = 0
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if flag == 0 and find(a) == find(b):
        flag = 1
        ans = i+1
    else:
        union(a, b)
print(ans)
"""

# 풀이를 정리하여 작성한 게시글
# 
"""
﻿안녕하세요, Python3 및 PyPy3 로 제출해보면서 풀 때, 저를 포함한 많은 분들이 이와 같은 에러를 겪지 않을까 싶어 남겨봅니다.
﻿
﻿1. 런타임 에러
﻿Union Find 를 구현할 때 재귀로 구현하다 보면, 런타임에러가 발생할 수 있습니다.
재귀로 인한 런타임 에러의 경우 ﻿코드 맨 윗줄에 아래와 같이 추가를 해주시면 됩니다.
﻿﻿import sys
sys.setrecursionlimit(10**6)
혹은 재귀함수를 while 문으로 변경하는 방법도 있습니다.
﻿(참고: ﻿﻿https://www.acmicpc.net/board/...﻿)

﻿while x != parent[x]:
    x = parent[x]

﻿﻿return x
﻿2. 메모리 초과

PyPy3 로 제출시 메모리 초과, Python3 로 제출시 시간 초과가 나는 현상은 아래와 같이 Union Find 최적화 방법으로 해결할 수 있습니다. Union Find 최적화 방법은 (1) Path Compression (경로 압축) 과 (2) Union by Rank 가 있습니다. 

(참고: ﻿https://algorithms.tutorialhor...﻿)
﻿(1) 경로압축은 find 함수에서 최상위 부모를 찾을 때마다, 부모를 이 때 찾은 최상위 부모로 업데이트하는 방식입니다. 이렇게 하면 나중에 동일한 값의 최상위 부모를 찾을 때, 시간이 엄청나게 절약됩니다.
﻿﻿def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]
(2) Union by Rank 는 아래와 같이 구현할 수 있습니다. 항상 작은 값 기준으로 혹은 항상 큰 값 기준으로합치도록 하면, 트리의 높이가 낮아져서 시간이 빨라지는 효과가 있습니다.
if parent[a] < parent[b]:
    parent[parent[a]] = parent[b]
else:
    parent[parent[b]] = parent[a]



3. 시간 초과

﻿시간초과가 나는 경우, 2번에서와 같이 (1), (2) 최적화 방법이 모두 적용되었는지 확인이 필요합니다. 그래도 시간 초과인 경우 input 함수로 입력을 받는게 시간이 오래 걸렸기 때문일 수 있습니다. 코드 맨 윗줄에 아래와 같이 추가하여 해결할 수 있습니다.

﻿﻿import sys
input = sys.stdin.readline﻿
"""
