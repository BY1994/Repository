"""
1551 수열의 변화

구현
"""

N, K = map(int, input().split())
arr = list(map(int, input().split(',')))
start = 0
while K:
    for i in range(N-1, start, -1):
        arr[i] -= arr[i-1]
    start += 1
    K -= 1

print(','.join(map(str, arr[start:])))
