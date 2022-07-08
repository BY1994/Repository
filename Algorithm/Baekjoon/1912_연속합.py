"""
1912 연속합

DP, 카데인 알고리즘 (최대 연속합 구하는 알고리즘)
https://kplog.tistory.com/273

이 문제의 정석에 대한 질문
https://www.acmicpc.net/board/view/77835
"""

# Kadane's Algorithm
n = int(input())
array = list(map(int, input().split()))
_sum = 0
max_val = -1000 * 100000

for i in range(n):
    _sum += array[i]
    max_val = max(max_val, _sum)

    if _sum < 0:
        _sum = 0

print(max_val)

# 다른 코드
# https://www.acmicpc.net/board/view/82341
"""
n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] = max(data[i], data[i] + data[i-1])
  
print(max(data))
"""
