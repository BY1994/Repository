"""
14565 역원 구하기

유클리드 호제법
https://kbw1101.tistory.com/53?category=778980
https://ssungkang.tistory.com/entry/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B3%BC-%ED%99%95%EC%9E%A5%EB%90%9C-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95#%ED%98%B8%EC%A0%9C%EB%B2%95%EC%9D%98_%ED%99%95%EC%9E%A5

14565 문제 설명
https://kau-algorithm.tistory.com/36
"""

#int q, r1, r2, r, s1, s2, s, t1, t2, t;

def gcd(a, b):
    return gcd(b, a%b) if b else a

def xgcd(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while True:
        q = r1 // r2
        r = r1 - (q * r2)
        s = s1 - (q * s2)
        t = t1 - (q * t2)

        #print(r2, s2, t2, q, r, s, t)
        if r == 0:
            # gcd: r2, s: s2, t: t2
            return s2 # inverse of multiply

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

N, A = map(int, input().split())
if gcd(A, N) != 1:
    inv = -1
else:
    inv = xgcd(A, N)
    while inv <= 0:
        inv += N

print(N-A, inv)
