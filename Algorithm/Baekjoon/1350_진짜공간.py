"""
1350 진짜 공간

수학
* 파일의 크기는 10억인데, N 이 50 이기 때문에 long long 크기로 봐야한다.
"""

N = int(input())
files = list(map(int, input().split()))
cluster = int(input())
ans = 0
for i in range(N):
    ans += (files[i]//cluster)*cluster
    if files[i] % cluster:
        ans += cluster
print(ans)
