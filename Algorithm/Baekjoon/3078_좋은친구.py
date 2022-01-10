"""
3078 좋은 친구

python3 시간 초과
pypy3 통과
"""

N, K = map(int, input().split())
K += 1
name = [0] * 21
friends = []
for i in range(N):
    friends.append(len(input()))

ans = 0
for i in range(K):
    name[friends[i]] += 1

# 첫번째 학생을 기점으로
ans += name[friends[0]]-1

#cur = ans
for i in range(K, N):
    name[friends[i-K]] -= 1
    name[friends[i]] += 1

    ans += name[friends[i-K+1]] - 1

for i in range(N-K+1, N):
    name[friends[i-1]] -= 1
    ans += name[friends[i]] - 1

print(ans)
