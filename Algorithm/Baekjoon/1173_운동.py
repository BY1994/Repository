"""
1173 운동

구현

질문 검색 게시판을 보면 사람들이 많이 틀리는 이유
1. -1 처리를 해주지 않아서 무한 루프
2. m 보다 작으면 m 으로 간주한다는 것 빼먹어서

이와 같은 풀이에 문제가 없다는 증명이나
더 빠른 간단한 방법이 없는지 궁금하다.
"""

N, m, M, T, R = map(int, input().split())
if m + T > M:
    print(-1)
else:
    ans = 0
    cur = m
    while N > 0:
        if cur + T <= M:
            cur += T
            N -= 1
        else:
            cur = max(cur - R, m)
        ans += 1
    print(ans)
