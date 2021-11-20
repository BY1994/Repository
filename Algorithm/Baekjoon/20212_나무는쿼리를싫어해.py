"""
20212 나무는 쿼리를 싫어해

세그먼트 트리
https://8iggy.tistory.com/173
https://ojt90902.tistory.com/532

파이썬 입출력 속도
https://www.acmicpc.net/board/view/61109

Lazy segment tree
https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/

(1)
내가 만들어본 큰 수 예시 => 틀렸습니다 일 듯
4
1 1 1 1000
1 1 1000000000 500
2 2 100 1
2 2 100 2

했더니 0 0 으로 오답이 나옴
정답은 0 49500

(2)
런타임 에러 (IndexError) 해결!
        # arr1 과 arr2는 index가 다름... dict 에러인 줄 알았는데...
        update(1, 0, newN-1, findAstart[arr1[cur][1]], findAend[arr1[cur][2]], arr1[cur][3])
"""
import sys

def init(i, left, right):
    if left == right:
        # 초기값 0 이므로 [i][2] 는 업데이트 불필요
        segment_tree[i][0] = newsetA[left][0]
        segment_tree[i][1] = newsetA[left][1]
        return segment_tree[i][0], segment_tree[i][1]
    mid = left + (right - left) // 2
    sa, ea = init(i * 2, left, mid)
    sb, eb = init(i * 2 + 1, mid + 1, right)
    segment_tree[i][0] = min(sa, sb)
    segment_tree[i][1] = max(ea, eb)
    return segment_tree[i][0], segment_tree[i][1]
 
def search(i, start, end, left, right):
    #print(f"### seg{segment_tree[i][2]} {segment_tree[i][1]}-{segment_tree[i][0]}*{lazy[i]}")
    if lazy[i] != 0:
        segment_tree[i][2] += (segment_tree[i][1]-segment_tree[i][0]+1)*lazy[i]
        if start != end:
            lazy[i*2] += lazy[i]
            lazy[i*2+1] += lazy[i]
        lazy[i] = 0

    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        #print(f"### seg{segment_tree[i][2]} {left}<={start} {end} <= {right}")
        return segment_tree[i][2]

    mid = start + (end - start) // 2
    return search(i * 2, start, mid, left, right)+ \
               search(i * 2 + 1, mid + 1, end, left, right)

def update(i, start, end, left, right, diff):
    #print(f"### seg{segment_tree[i][2]} {segment_tree[i][1]}-{segment_tree[i][0]}*{lazy[i]}")
    if lazy[i] != 0:
        segment_tree[i][2] += (segment_tree[i][1]-segment_tree[i][0]+1)*lazy[i]
        if start != end:
            lazy[i*2] += lazy[i]
            lazy[i*2+1] += lazy[i]
        lazy[i] = 0

    if end < left or right < start:
        #print(f"### seg0 {left}>{end} {start} > {right}")
        return 0

    if start >= left and end <= right:
        #print(f"### seg{segment_tree[i][2]} {left}<={start} {end} <= {right}")
        segment_tree[i][2] += (segment_tree[i][1]-segment_tree[i][0]+1)*diff
        if start != end:
            lazy[i*2] += diff
            lazy[i*2+1] += diff
        #print("### segment_tree1")
        #print(segment_tree)
        #print()
        #print(lazy)
    else:
        #print(f"### seg{segment_tree[i][2]} {left}!<={start} {end} !<= {right}")
        mid = start + (end - start) // 2
        update(i*2, start, mid, left, right, diff)
        update(i*2+1, mid+1, end, left, right, diff)
        segment_tree[i][2] = segment_tree[i*2][2] + \
                   segment_tree[i*2+1][2]

        #print("### segment_tree2")
        #print(segment_tree)
        #print()
        #print(lazy)

N = int(input())
arr1 = []
arr2 = []
#A = []
setA = set()

arr2cnt = 0
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 1:
        arr1.append(tmp)
    else:
        tmp[0] = arr2cnt
        arr2.append(tmp)
        arr2cnt += 1
    #A.append([i, arr[i][1]])
    #A.append([i, arr[i][2]])
    setA.add(tmp[1])
    setA.add(tmp[2])

setA = list(setA)
setA.sort() # sort를 안 해서 dict 에서 못 찾아서 그렇다고 생각
newN = len(setA)
newsetA = []
for i in range(newN-1):
    newsetA.append([setA[i], setA[i]])
    if setA[i] +1 <= setA[i+1]-1:
        newsetA.append([setA[i]+1, setA[i+1]-1])

newsetA.append([setA[newN-1], setA[newN-1]])

newN = len(newsetA)

#A.sort(key=lambda x:x[1]) # arg2
findAstart = {}
findAend = {}
for i in range(newN):
    #findAstart[(setA[i], setA[i+1])] = i
    findAstart[newsetA[i][0]] = i
    findAend[newsetA[i][1]] = i
#findA = dict(zip(setA, list(range(newN))))
#findA.sort(key=lambda x:x[0]) # arg0

arr2.sort(key=lambda x:x[3])

segment_tree = [[0, 0, 0] for _ in range(4*newN)]
lazy = [0]*4*newN

init(1, 0, newN-1)
cur = 0
ans = [0] * arr2cnt
for i in range(arr2cnt):
    while arr2[i][3] > cur:
        #print(f"#{findAstart[arr1[i][1]]}~{findAend[arr1[i][2]]}")
        # arr1 과 arr2는 index가 다름... dict 에러인 줄 알았는데...
        update(1, 0, newN-1, findAstart[arr1[cur][1]], findAend[arr1[cur][2]], arr1[cur][3])
        cur += 1

    #print(f"{findAstart[arr2[i][1]]}~{findAend[arr2[i][2]]}")
    ans[arr2[i][0]] = search(1, 0, newN-1, findAstart[arr2[i][1]], findAend[arr2[i][2]])
    #print(ans[arr2[i][0]])

for i in range(arr2cnt):
    print(ans[i])
