"""
2042 구간 합 구하기

세그먼트 트리
https://8iggy.tistory.com/173

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109
"""
import sys

def init(i, left, right):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = init(i * 2, left, mid) + \
        init(i * 2 + 1, mid + 1, right)
    return segment_tree[i]
 
def search(i, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return search(i * 2, start, mid, left, right) + \
               search(i * 2 + 1, mid + 1, end, left, right)

def update(i, start, end, idx, diff):
    if start > idx or idx > end:
        return
    segment_tree[i] += diff
    if start != end:
        mid = start + (end-start) // 2
        update(i*2, start, mid, idx, diff)
        update(i*2+1, mid+1, end, idx, diff)

N, M, K = map(int, sys.stdin.readline().split())
segment_tree =[0]*4*N

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
init(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, 0, N-1, b-1, c-arr[b-1])
        arr[b-1] = c
    else:
        print(search(1, 0, N-1, b-1, c-1))
