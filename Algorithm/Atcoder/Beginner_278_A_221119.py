N, K = map(int, input().split())
A = input().split()
if K > N:
    K = N
print(*A[K:], *([0]*K))
