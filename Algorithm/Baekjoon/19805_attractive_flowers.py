"""
19805 Attractive Flowers

greedy

마지막 수 더할 때 odd인지 고려를 안 해서 틀림
"""


N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
ans = 0
for i in range(N):
    flower = numbers[i] - ((numbers[i]+1) % 2)
    if i == N-1:
        if (ans + flower) % 2 == 0: continue
    ans += flower

print(ans)

# 홀수 구하는 거니까 마지막 비트 가지고 뺄 수도 있음
# https://www.acmicpc.net/source/22599378
"""
input()
n=sorted(i-(i&1^1)for i in map(int,input().split()))
s=sum(n[len(n)&1^1:])
print(s-(s&1^1))
"""
