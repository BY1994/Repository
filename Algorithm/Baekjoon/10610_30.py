"""
10610 30

30 의 배수 찾기
그리디
"""

N = input()
lenN = len(N)
count = [0]*10
zero = ord('0')
for i in range(lenN):
    count[ord(N[i])-zero] += 1

ans = [0]*lenN
ind = 0
total = 0
for i in range(9, -1, -1):
    while count[i]:
        ans[ind] = i
        ind += 1
        count[i] -= 1
        total += i

if total % 3: # 3의 배수
    print(-1)
elif ans[ind-1]: # 10의 배수
    print(-1)
else:
    print(*ans, sep="")


