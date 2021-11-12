"""
5675 음주 코딩

세그먼트 트리
https://8iggy.tistory.com/173
https://ojt90902.tistory.com/532

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109

파이썬 ValueError
https://www.acmicpc.net/board/view/74992
"""
import sys

def init(i, left, right):
    if left == right:
        if arr[left] > 0:
            segment_tree[i] = 1
        elif arr[left] < 0:
            segment_tree[i] = -1
        else:
            segment_tree[i] = 0
        return segment_tree[i]
    mid = left + (right - left) // 2
    segment_tree[i] = init(i * 2, left, mid) * \
        init(i * 2 + 1, mid + 1, right)
    return segment_tree[i]
 
def search(i, start, end, left, right):
    if end < left or right < start:
        return 1
    if left <= start and end <= right:
        return segment_tree[i]
    mid = start + (end - start) // 2
    return search(i * 2, start, mid, left, right) * \
               search(i * 2 + 1, mid + 1, end, left, right)

def update(i, start, end, idx, value):
    if end < idx or idx < start:
        return 1
    if start == end == idx:
        if value > 0:
            segment_tree[i] = 1
        elif value < 0:
            segment_tree[i] = -1
        else:
            segment_tree[i] = 0
        return segment_tree[i]
    mid = start + (end - start) // 2
    update(i*2, start, mid, idx, value)
    update(i*2+1, mid+1, end, idx, value)
    segment_tree[i] = segment_tree[i*2] * \
               segment_tree[i*2+1]
    return segment_tree[i]

while(True):
    try:
        N, K = map(int, sys.stdin.readline().split())
        segment_tree =[1]*4*N

        arr = list(map(int, sys.stdin.readline().split()))

        init(1, 0, N-1)
        for _ in range(K):
            cmd, i, j = sys.stdin.readline().split()
            if cmd == "C":
                update(1, 0, N-1, int(i)-1, int(j))
            else:
                ans = search(1, 0, N-1, int(i)-1, int(j)-1)
                if ans > 0:
                    print("+", end="")
                elif ans < 0:
                    print("-", end="")
                else:
                    print("0", end="")
        print()
    except Exception:
        break
