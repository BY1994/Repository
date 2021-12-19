"""
12738 가장 긴 증가하는 부분 수열 3

바이너리 서치 코드
https://brownbears.tistory.com/565
"""
import sys

# 가지치기니까 backtracking
def dfs(cur, depth, n):
    global flag
    if flag == 1:
        return True
    if depth >= n:
        flag = 1
        return True
    ret = 0
    for i in range(cur+1, N):
        if A[i] > A[cur]:
            ret = max(ret, dfs(i, depth+1, n))
    return ret

def pos(n):
    global N, flag
    ans = 0
    for i in range(N):
        flag = 0
        ans = max(dfs(i, 1, n), ans)
    return ans

#def binary_search(arr, value):
def binary_search(n):
    first, last = 1, n

    while first <= last:
        mid = (first + last) // 2
        #if arr[mid] == value:
        #    return mid
        if pos(mid): # ok
            ans = mid
            first = mid + 1
        else: # not ok
            last = mid - 1

        #if arr[mid] > value:
        #    last = mid - 1
        #else:
        #    first = mid + 1

    return ans

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

flag = 0
print(binary_search(N))
