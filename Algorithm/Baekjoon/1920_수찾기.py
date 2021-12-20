"""
1920 수 찾기

이분 탐색이 꼭 필요한가?
=> 인풋이 너무 커서 꼭 필요하다

https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""

# 이분탐색으로 풀고 통과
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range(M):
    #binary_search()
    left = 0 
    right = N-1
    mid = 0

    while left<=right:
        mid = (left+right)//2
        if A[mid] == B[i]:
            print(1)
            break
        elif A[mid]> B[i]:
            right = mid-1
        else :
            left = mid+1
    else:
        print(0)

# https://www.acmicpc.net/source/35893905
# python 은 in 이 있으니까 이렇게 어렵게 쓸 필요 없음
"""
import os, io,sys
I=io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
I()
s=set(I().split())
I()
for x in I().split():sys.stdout.write('1\n'if x in s else'0\n')
"""


# 다시 풀자
"""
N = int(input())
A = map(int, input().split())
M = int(input())
X = map(int, input().split())

nums = [0] * (N+1)
for a in A:
    nums[a] = 1

for x in X:
    print(int(nums[x] == 1))
"""
