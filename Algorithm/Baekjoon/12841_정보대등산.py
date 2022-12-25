"""
12841 정보대 등산

brute force
"""

n = int(input())
cross = list(map(int, input().split()))
left = list(map(int, input().split()))
right = list(map(int, input().split()))
left_sum = [0]*n
right_sum = [0]*n

for i in range(n-1):
    left_sum[i+1] = left[i] + left_sum[i]
    right_sum[i+1] = right[i] + right_sum[i]

min_ind = 0
min_value = 20000000000
for i in range(n):
    ans = left_sum[i]
    ans += cross[i]
    ans += right_sum[n-1] - right_sum[i]
    if min_value > ans:
        min_value = ans
        min_ind = i+1

print(min_ind, min_value)
