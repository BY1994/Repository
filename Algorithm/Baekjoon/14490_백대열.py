"""
14490 백대열

유클리드 호제법
"""

def gcd(n, m):
    return gcd(m, n%m) if m else n

numbers = input().split(':')
n = int(numbers[0])
m = int(numbers[1])

g = gcd(n, m)
print(f"{n//g}:{m//g}")


#숏코딩
"""
n,m=map(int,input().split(':'))
a,b=n,m
while b>0:a,b=b,a%b
print(n//a,':',m//a,sep='')
"""
