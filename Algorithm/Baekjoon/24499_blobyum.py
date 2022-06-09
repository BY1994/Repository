"""
24499 blobyum

누적합으로 안 풀고 슬라이딩 윈도우로 해결
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

# init
cur = 0
for i in range(K):
    cur += A[i]
maxv = cur

# sliding window
for i in range(1,N):
    cur -= A[i-1]
    cur += A[(i-1+K) % N]
    maxv = max(cur, maxv)

print(maxv)
