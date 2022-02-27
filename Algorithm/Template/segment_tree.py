"""
세그먼트 트리
https://8iggy.tistory.com/173
https://ojt90902.tistory.com/532

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109
"""
import sys

def init(i, left, right):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = min(init(i * 2, left, mid), \
        init(i * 2 + 1, mid + 1, right))
    return segment_tree[i]

def search(i, start, end, left, right):
    if end < left or right < start:
        return 1000000000
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return min(search(i * 2, start, mid, left, right), \
               search(i * 2 + 1, mid + 1, end, left, right))

def update(i, start, end, idx, value):
    if end < idx or idx < start:
        return 1000000000
    if start == end == idx:
        segment_tree[i] = value
        return value
    mid = start + (end - start) // 2
    update(i*2, start, mid, idx, value)
    update(i*2+1, mid+1, end, idx, value)
    segment_tree[i] = min(segment_tree[i*2], \
               segment_tree[i*2+1])
    return segment_tree[i]

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
segment_tree =[1000000000]*4*N
init(1, 0, N-1)
M = int(input())
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(search(1, 0, N-1, b-1, c-1))
