T = int(input())

for tc in range(1, T+1):
    S = input()
    ans = ""
    con = 1
    for i in range(len(S)-1):
        if S[i] < S[i+1]:
            ans += S[i]*(con+1)
            con = 1
        elif S[i] == S[i+1]:
            ans += S[i]
            con += 1
        else:
            ans += S[i]
            con = 1
    ans += S[-1]
    print(f"Case #{tc}: {ans}")
