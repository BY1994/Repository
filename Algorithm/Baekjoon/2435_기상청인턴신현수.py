"""
2435 기상청 인턴 신현수

K 길이 만큼의 구간의 합 구하기
이건 sliding window 라고 봐야하는 거 아닌가?
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
ans = sum(temp[:K])
cur = ans

for i in range(N-K):
    cur -= temp[i]
    cur += temp[i+K]

    if cur > ans:
        ans = cur

print(ans)
