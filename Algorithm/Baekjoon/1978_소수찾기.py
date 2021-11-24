"""
1978 소수 찾기
"""

N = int(input())
nums = map(int, input().split())

nprime = 0
for i in nums:
    if i == 1:
        nprime += 1
    
    for j in range(i-1, 1, -1):
        if i % j == 0:
            nprime +=1
            break

print(N - nprime)



# https://www.acmicpc.net/source/18191610
"""
n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)
"""
