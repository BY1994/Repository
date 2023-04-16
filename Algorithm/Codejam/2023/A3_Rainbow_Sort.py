"""
Codejam2023 A round
Rainbow Sort

1 번도 3번도 dict 를 이용하면 너무 간단했던 문제
이미 값이 존재하는지 확인하고, 존재하면 불가능한 것으로 출력하기
"""

for tc in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    print(f"Case #{tc+1}: ", end="")
    d = {}
    flag = 0
    for i in range(N):
        if i > 0 and S[i] == S[i-1]:
            continue
        if S[i] in d:
            flag = 1
            break
        else:
            d[S[i]] = 1
    if flag:
        print(f"IMPOSSIBLE")
    else:
        print(*d.keys())
