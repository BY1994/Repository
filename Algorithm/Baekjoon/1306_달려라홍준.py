"""
1306 달려라 홍준

최댓값 세그먼트 트리

python3 로 제출시 시간 초과,
pypy3로 제출시 맞았습니다. (5192 ms)

다른 풀이로 푼다면,
sliding window 범위 안에 숫자들을 counting 해두고,
앞에거는 - 시키고, 0 되는지 보고,
뒤에거는 + 시키고, 1 되는지 봐야할 듯
"""
import sys

def init(i, left, right):
    if left == right:
        segment_tree[i] = arr[left]
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = max(init(i * 2, left, mid), \
        init(i * 2 + 1, mid + 1, right))
    return segment_tree[i]

def search(i, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return max(search(i * 2, start, mid, left, right), \
               search(i * 2 + 1, mid + 1, end, left, right))

N, M  = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# segment tree
segment_tree =[0]*4*N

init(1, 0, N-1)


# 시간 초과 해결하기: print를 매번 하지 말기?
# 이걸로 해결 안 됨. python3 -> pypy3 로 제출하고 성공

ans = []
# print answer
for i in range(M, N-M+2):
    ans.append(search(1, 0, N-1, i-M, i+M-2))

print(*ans)
"""
# print answer
for i in range(M, N-M+2):
    print(search(1, 0, N-1, i-M, i+M-2), end=" ")
"""
