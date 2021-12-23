"""
10815 숫자 카드

이분 탐색
https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

시간 단축 방법
(local 변수 사용시 더 빠름)
https://www.acmicpc.net/board/view/68809
https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function
"""
import sys

def binary_search(n):
    global N
    ans = 0
    left = 0#-10000000 
    right = N-1 #10000000
    mid = 0

    while left<=right:
        mid = (left+right)//2
        if cards[mid] == n:
            return 1
        if cards[mid] < n:
            left = mid+1
        else:
            right = mid - 1
    return 0

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
for i in numbers:
    print(binary_search(i), end=" ")
