"""
1592 영식이와 친구들

구현 시뮬레이션
조세푸스 같은 느낌
% 연습하기 좋은 문제
"""

N, M, L = map(int, input().split())
ans = 0
cnt = [0] * (N+1)
cur = 1
cnt[cur] += 1
while cnt[cur] < M:
    if cnt[cur] % 2:
        cur = (cur-1+L)%N + 1
    else:
        cur = (cur-1+N-L)%N + 1
    ans += 1
    cnt[cur] += 1
print(ans)
