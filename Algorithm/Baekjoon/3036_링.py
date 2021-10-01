"""
3036 링

유클리드 호제법 = 최대 공약수 구하는 방법

4
7 12 14 28

7/12
1/2
1/4
https://www.acmicpc.net/board/view/11577

반례
https://www.acmicpc.net/board/view/33802

"""

def gcd(m, n):
    if n == 0: return m
    return gcd(n, m % n)

N = int(input())
numbers = list(map(int, input().split()))

for i in range(N-1):
    g = gcd(numbers[0], numbers[i+1])
    print(f"{numbers[0]//g}/{numbers[i+1]//g}")

# 조건을 더 숏코딩하려면 예시 (C)
"""
int f(int x,int y){return y?f(y,x%y):x;}int n,t;main(u){scanf("%d%d",&n,&t);while(--n){scanf("%d",&u);printf("%d/%d\n",t/f(t,u),u/f(t,u));}}
"""

# 조건을 더 숏코딩하려면 예시 (python)
"""
def GCD(a,b): return GCD(b,a%b) if b else a
"""

"""
def gcd(m, n):
    while n > 0:
        temp = m
        m = n
        n = temp % n
    return m

N = int(input())
numbers = list(map(int, input().split()))

for i in range(N-1):
    g = gcd(numbers[0], numbers[i+1])
    print(f"{numbers[0]//g}/{numbers[i+1]//g}")
"""
