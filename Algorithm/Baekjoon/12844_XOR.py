"""
12844 XOR

세그먼트 트리
https://8iggy.tistory.com/173
https://ojt90902.tistory.com/532

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109

Lazy segment tree
https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/
"""
import sys

def init(i, left, right):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = init(i * 2, left, mid)^ \
        init(i * 2 + 1, mid + 1, right)
    return segment_tree[i]
 
def search(i, start, end, left, right):
    if lazy[i] != 0:
        segment_tree[i] ^= ((end-start+1)%2)*lazy[i]
        if start != end:
            lazy[i*2] ^= lazy[i]
            lazy[i*2+1] ^= lazy[i]
        lazy[i] = 0

    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return search(i * 2, start, mid, left, right)^ \
               search(i * 2 + 1, mid + 1, end, left, right)

def update(i, start, end, left, right, xor):
    if lazy[i] != 0:
        segment_tree[i] ^= ((end-start+1)%2)*lazy[i] # xor 아님!!
        if start != end:
            lazy[i*2] ^= lazy[i]
            lazy[i*2+1] ^= lazy[i]
        lazy[i] = 0

    if end < left or right < start:
        return 0

    if start >= left and end <= right:
        segment_tree[i] ^= ((end-start+1)%2)*xor
        if start != end:
            lazy[i*2] ^= xor
            lazy[i*2+1] ^= xor
    else:
        mid = start + (end - start) // 2
        update(i*2, start, mid, left, right, xor)
        update(i*2+1, mid+1, end, left, right, xor)
        segment_tree[i] = segment_tree[i*2]^ \
                   segment_tree[i*2+1]

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
# 초기에는 꺼져있는 상태
segment_tree = [0]*4*N
lazy = [0] *4*N
init(1, 0, N-1)
for _ in range(int(input())):
    _input = list(map(int, sys.stdin.readline().split()))
    if _input[0] == 1:
        update(1, 0, N-1, _input[1], _input[2], _input[3])
    else:
        print(search(1, 0, N-1, _input[1], _input[2]))
