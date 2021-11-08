"""
2357 최솟값과 최댓값

세그먼트 트리
https://8iggy.tistory.com/173

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109
"""
import sys

def min_init(i, left, right):
    if left == right:
        min_segment_tree[i] = arr[left]
        return min_segment_tree[i]
    mid = left + (right - left) // 2
    min_segment_tree[i] = min(min_init(i * 2, left, mid), \
        min_init(i * 2 + 1, mid + 1, right))
    return min_segment_tree[i]

def max_init(i, left, right):
    if left == right:
        max_segment_tree[i] = arr[left]
        return max_segment_tree[i]
    mid = left + (right - left) // 2
    max_segment_tree[i] = max(max_init(i * 2, left, mid), \
        max_init(i * 2 + 1, mid + 1, right))
    return max_segment_tree[i]
 
def min_search(i, start, end, left, right):
    if end < left or right < start:
        return 1000000000
    if left <= start and end <= right:
        return min_segment_tree[i]
    mid = start + (end - start) // 2
    return min(min_search(i * 2, start, mid, left, right), \
               min_search(i * 2 + 1, mid + 1, end, left, right))
 
def max_search(i, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return max_segment_tree[i]
    mid = start + (end - start) // 2
    return max(max_search(i * 2, start, mid, left, right), \
               max_search(i * 2 + 1, mid + 1, end, left, right))

N, M = map(int, sys.stdin.readline().split())
min_segment_tree =[1000000000]*4*N
max_segment_tree =[0]*4*N

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
min_init(1, 0, N-1)
max_init(1, 0, N-1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(min_search(1, 0, N-1, a-1, b-1), max_search(1, 0, N-1, a-1, b-1))

# 시간초과
"""
def init(i, left, right):
    if left == right:
        segment_tree[i][0] = arr[left]
        segment_tree[i][1] = arr[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i][0] = min(init(i * 2, left, mid)[0], \
        init(i * 2 + 1, mid + 1, right)[0])
    segment_tree[i][1] = max(init(i * 2, left, mid)[1], \
        init(i * 2 + 1, mid + 1, right)[1])
    return segment_tree[i]
 
 
def search(i, start, end, left, right):
    if end < left or right < start:
        return [1000000000, 0]
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return [min(search(i * 2, start, mid, left, right)[0], \
               search(i * 2 + 1, mid + 1, end, left, right)[0]), \
            max(search(i * 2, start, mid, left, right)[1], \
               search(i * 2 + 1, mid + 1, end, left, right)[1])]
 

N, M = map(int, input().split())
segment_tree =[[1000000000, 0] for _ in range(4*N)]
arr = []
for _ in range(N):
    arr.append(int(input()))
init(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*search(1, 0, N-1, a-1, b-1))
"""
