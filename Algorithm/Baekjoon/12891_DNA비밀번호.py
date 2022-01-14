"""
12891 DNA 비밀번호
"""

S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())
a, c, g, t = 0, 0, 0, 0

ans = 0
std = 0
for i in range(P):
    if DNA[i] == 'A':
        a += 1
    elif DNA[i] == 'C':
        c += 1
    elif DNA[i] == 'G':
        g += 1
    elif DNA[i] == 'T':
        t += 1

if a >= A and c >= C and g >= G and t >= T:
    ans += 1
    
for i in range(S-P):
    if DNA[i] == 'A':
        a -= 1
    elif DNA[i] == 'C':
        c -= 1
    elif DNA[i] == 'G':
        g -= 1
    elif DNA[i] == 'T':
        t -= 1

    if DNA[i+P] == 'A':
        a += 1
    elif DNA[i+P] == 'C':
        c += 1
    elif DNA[i+P] == 'G':
        g += 1
    elif DNA[i+P] == 'T':
        t += 1

    if a >= A and c >= C and g >= G and t >= T:
        ans += 1

print(ans)
