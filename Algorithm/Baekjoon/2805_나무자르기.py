"""
2805 나무 자르기

이분 탐색
https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

시간 단축 방법
(local 변수 사용시 더 빠름)
https://www.acmicpc.net/board/view/68809
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function
"""

import sys

def check(n):
    ret = 0
    for i in trees:
        if i > n: # ret += max(0, i-n)
            ret += i-n
    return ret

def binary_search(left, right):
    ans = 0
    #left = 0 
    #right = max(trees) #1000000000
    mid = 0
    ans = 0

    while left<=right:
        mid = (left+right)//2
        if check(mid) >= M:
            ans = mid
            left = mid+1
        else:
            right = mid - 1
    return ans

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


print(binary_search(0, max(trees)))
