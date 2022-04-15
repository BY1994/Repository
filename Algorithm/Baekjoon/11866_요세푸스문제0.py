"""
11866 요세푸스 문제 0
"""

N, K = map(int, input().split())
alive = [0] * 1001
remain = N
cur = 0
count = 0

print('<', end="")
print(K, end="")
alive[K-1] = 1
cur = K % N
remain -=1

while remain:
    if alive[cur] == 1:
        cur = (cur+1) % N
        continue
    count += 1
    if count % remain == K % remain:
        count = 0
        remain -= 1
        alive[cur] = 1
        print(",", cur+1, end="")
    cur = (cur+1) % N
print('>')
