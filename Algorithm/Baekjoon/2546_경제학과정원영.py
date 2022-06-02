"""
2546 경제학과 정원영

시간 초과 -> sum 을 미리 안 구하고 매번 구하게 했더니 시간초과가 났다.
N 은 최대 200,000
시간 제한 1초
"""

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    input()
    N, M = map(int, input().split())
    Cs = list(map(int, input().split()))
    Ecos = list(map(int, input().split()))

    sum_Cs = sum(Cs)
    sum_Ecos = sum(Ecos)

    avg_Cs = sum_Cs / N
    avg_Ecos = sum_Ecos / M    

    ans = 0
    for i in range(N):
        if (sum_Cs - Cs[i]) / (N-1) > avg_Cs:
            if (sum_Ecos + Cs[i]) / (M+1) > avg_Ecos:
                ans += 1

    print(ans)
