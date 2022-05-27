"""
1145 적어도 대부분의 배수

완전 탐색도 가능하다. 모든 숫자로 3개 이상 배수되는 거 있는지 검사하는 거.
처음에 아래처럼 풀 때 실수한 부분은
gcd(i, j)
gcd(g, k) 이렇게 3개의 gcd 를 한번에 구해서 i/g*j/g*k 하면 나온다고 착각했던 것
그렇게 되면 1, 2, 4 인 경우에 gcd 가 1이 나와서 배수를 구해보면 최소 공배수인 4가 아니라 8이 나오게 된다.
두 수의 최소 공배수를 한 번 구해주고, 그 수와 함께 다시 최소 공배수를 구해야한다.
"""

def gcd(a, b):
    return gcd(b, a%b) if b else a

numbers = list(map(int, input().split()))
ans = 1000001
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            g1 = gcd(numbers[i], numbers[j])
            g2 = gcd(numbers[i]*numbers[j]//g1, numbers[k])
            ans = min(ans, (numbers[i]*numbers[j]//g1)*numbers[k]//g2)
print(ans)
