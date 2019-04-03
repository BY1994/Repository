"""
11049 행렬 곱셈 순서
"""

N = int(input())
memo = [[-1 for _ in range(N)] for __ in range(N)]
array = []
minsum = 2**31
for _ in range(N):
    r, c = map(int, input().split())
    array.append([r, c])

order = [0] * (N-1) # 요소들의 인덱스 저장
used = [False] * (N-1) 

def perm(k, cursum): # k: 노드의 높이(=지금까지 선택한 수), n: 트리의 높이 (내가 해야할 전체 선택 수)
    global N
    if k == N-1:
        # 하나의 순열 생성
        print(order)
        return
    else:
        # 가능한 선택지를 계산
        # 이미 한 선택(k개)을 확인한다.            
        for i in range(N-1):
            if used[i]:
                if 
                continue
            order[k] = i
            used[i] = True
            perm(k + 1, cursum)
            used[i] = False # 나올 때 다시 복구
perm(0, 3)

"""
perms = [0] * (N-1)
# 필요한 곱셈 연산의 최솟값....
# 순열 뽑아내기
def permutation(depth, cursum):
    global minsum
    if depth == N:
        # 그때의 최소값을 비교
        if cursum < minsum:
            minsum = cursum
    else:
        used = [False] * n
        for i in range(N-1):
            used[perms[i]] = True
        for i in range(N-1):
            if used[perms[i]]: continue
            perms[i] = i
            # 여기까지의 cursum
            
            permutation(depth+1, cursum+)
"""
