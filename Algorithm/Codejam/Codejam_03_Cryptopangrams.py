# Qualification Round 2019 - 3 Cryptopangrams
# 2019.04.06 PBY
"""
input)
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543
"""

# attempt 1 (Runtime Error)
"""
def primes_up_to(n: int) -> [int]:
    seive = [False, False] + [True] * (n-1)
    for (i, e) in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return [x for (x, y) in enumerate(seive) if y ]
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z']

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    code = list(map(int, input().split()))
    # prime numbers 
    primes = primes_up_to(N)
    # 처음 두 수 가지고 공통된 소수를 골라내야한다.
    anslist = []
    for i in primes:
        if code[0] % i == 0:
            a = i
            b = code[0] // i
            break
    if code[1] % a == 0:
        anslist.extend([b,a])
    else:
        anslist.extend([a,b])

    for i in range(1, L):
        anslist.append(code[i] // anslist[-1])
    
    primelist = sorted(set(anslist)) # 26?
    
    ans = ''
    for a in anslist:
        ans += alpha[primelist.index(a)]
    
    print("Case #{}: {}".format(tc, ans))
"""

# attempt 2
def primes_up_to(n: int) -> [int]:
    seive = [False, False] + [True] * (n-1)
    for (i, e) in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return [x for (x, y) in enumerate(seive) if y ]
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z']


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    code = list(map(int, input().split()))
    # prime numbers 
    primes = primes_up_to(N+1)
    # 처음 두 수 가지고 공통된 소수를 골라내야한다.
    anslist = []
    for i in primes:
        if code[0] % i == 0:
            a = i
            b = code[0] // i
            break
    if code[1] % a == 0:
        anslist.extend([b,a])
    else:
        anslist.extend([a,b])

    for i in range(1, L):
        anslist.append(code[i] // anslist[-1])
    
    primelist = sorted(set(anslist)) # 26?
    
    ans = ''
    for a in anslist:
        ans += alpha[primelist.index(a)]
    
    print("Case #{}: {}".format(tc, ans))

