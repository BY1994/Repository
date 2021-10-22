"""
20052 괄호 문자열

s-1 보다 s가 커야한다는 건 알겠는데,
e와 s-1을 비교하는 것은?

(()(()
121232


(()((
1
1 5
0

(()((
1
2 3
오답으로 자꾸 0이 나옴
=> search 함수 안에서 return 을 0으로 하는 바람에 최솟값이 0으로 자꾸 계산됨 
https://kth990303.tistory.com/m/170
https://8iggy.tistory.com/173

세그트리 배열 크기
https://yabmoons.tistory.com/431

이 문제는 Python 3로는 시간 초과가 난다
Python 3로 풀고 싶으면 union find (disjointset) 을 써야한다.

세그먼트 트리로 풀고 싶으면 pypy로 내야한다.
"""


def init(i, left, right):
    if left == right:
        segment_tree[i] = prefixsum[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = min(init(i * 2, left, mid), \
        init(i * 2 + 1, mid + 1, right))
    return segment_tree[i]
 
 
def search(i, start, end, left, right):
    if end < left or right < start:
        return 100010 # 여길 0 으로 하면 오답임
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return min(search(i * 2, start, mid, left, right), \
               search(i * 2 + 1, mid + 1, end, left, right))
 

string = input()
count = 0
# 1. prefix sum (구간 합)
prefixsum = [0] * 100010
N = len(string)+1
for i in range(N-1):
    prefixsum[i+1] = prefixsum[i] + (1 if string[i] == '(' else -1)
# 2. segment tree with min

segment_tree =[0]*4*N
init(1, 0, N-1)
# 3. query
for _ in range(int(input())):
    s, e = map(int, input().split())
    # 한 번이라도 ) 가 더 많이 나와서 음수되는 적이 있는지
    # and 여는 괄호와 닫는 괄호의 개수가 동일한지
    if search(1,0,N-1,s,e) >= prefixsum[s-1] and prefixsum[e] == prefixsum[s-1]:
        count += 1
print(count)

# 시간초과
"""
def init(arr, tree, i, left, right):
    if left == right:
        tree[i] = arr[left]
        return tree[i]
    mid = left + (right - left) // 2
    tree[i] = min(init(arr, tree, i * 2, left, mid), \
        init(arr, tree, i * 2 + 1, mid + 1, right))
    return tree[i]
 
 
def search(tree, i, start, end, left, right):
    if end < left or right < start:
        return 100010 # 여길 0 으로 하면 오답임
    if left <= start and end <= right:
        return tree[i]
    mid = start + (end - start) // 2
    return min(search(tree, i * 2, start, mid, left, right),search(tree, i * 2 + 1, mid + 1, end, left, right))
 

string = input()
count = 0
# 1. prefix sum (구간 합)
prefixsum = [0]
for i in range(len(string)):
    prefixsum.append(prefixsum[-1] + (1 if string[i] == '(' else -1))
# 2. segment tree with min
N = len(prefixsum)
segment_tree =[0]*4*N
init(prefixsum, segment_tree, 1, 0, N-1)
# 3. query
for _ in range(int(input())):
    s, e = map(int, input().split())
    # 한 번이라도 ) 가 더 많이 나와서 음수되는 적이 있는지
    # and 여는 괄호와 닫는 괄호의 개수가 동일한지
    if search(segment_tree, 1,0,N-1,s,e) >= prefixsum[s-1] and prefixsum[e] == prefixsum[s-1]:
        count += 1
print(count)
"""
