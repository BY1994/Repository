"""
Codejam2023 A round
Colliding Encoding

ABC 는 012 로 인코딩되고, BC 는 12 로 인코딩되는데
숫자로 넣으면 012와 12가 같아지길래 길이도 dict 에 추가하였다.
python3 로 제출하면 시간초과가 나서 pypy3 로 제출했는데 통과하였다.
"""

for tc in range(int(input())):
    D = list(map(int, input().split()))
    N = int(input())
    letterdict = {}
    flag = 0
    for i in range(N):
        S = input()
        cur = 0
        lenS = len(S)
        for j in range(lenS):
            cur *= 10
            cur += D[ord(S[j])-65]
        if (cur, lenS) in letterdict:
            flag = 1
        else:
            letterdict[(cur, lenS)] = 1
    if flag:
        print(f"Case #{tc+1}: YES")
    else:
        print(f"Case #{tc+1}: NO")
