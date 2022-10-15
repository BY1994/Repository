"""
1284 집 주소
"""
size = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    ans = 0
    while N:
        ans += size[N % 10]
        count += 1
        N //= 10
    print(ans + count + 1)

# 다른 풀이
# https://www.acmicpc.net/source/45793234
"""
main(t,n){for(;t=scanf("%d",&n),n;printf("%d ",t))for(;n;n/=10)t+=n%10<2?n&1?3:5:4;}
"""
