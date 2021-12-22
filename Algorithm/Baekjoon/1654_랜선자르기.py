"""
1654 랜선 자르기

이분 탐색
https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

시간 단축 방법
(local 변수 사용시 더 빠름)
https://www.acmicpc.net/board/view/68809
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function
"""

def check(n):
      ret = 0
      for i in lan:
          ret += i // n
      return ret
      
def binary_search(left, right):
    global N
    ans = 0
    #left = 0 
    #right = max(trees) #1000000000
    mid = 0

    while left<=right:
        mid = (left+right)//2
        if check(mid) >= N:
            ans = mid
            left = mid+1
        else:
            right = mid - 1
    return ans

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

print(binary_search(1,max(lan)))
