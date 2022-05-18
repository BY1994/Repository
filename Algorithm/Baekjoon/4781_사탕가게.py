"""
4781 사탕가게

처음에 냅색 풀 때 for 문 순서를 틀렸었는데,
그렇게하면 중복된 데이터가 자꾸 들어갔기 때문
근데 이 문제는 중복을 일부러 해야하기 때문에
그 for 문 순서로 해야 답이 된다!

N / (2의 거듭제곱)의 꼴로 나타낼 수 없는 모든 실수는 정확하게 표현되지 않아서 그래요.

https://www.acmicpc.net/board/view/82054
int로 바꿀 땐 소숫점 아래를 버리는데 대부분은 정확히 나오지만 0.29같은 몇몇 수들이 100을 곱하면 28.999999...
이런 식으로 자연수보다 살짝 작게 나와서 이런걸 방지하려고 적당한 작은 수를 더해서 소숫점 아래를 버림해도 문제 없도록 하는거에요.

틀렸습니다가 나온 이유
이차원배열처럼 DP[j] 에 DP[j-1] 을 고려해야하는 줄 알고...
"""

import sys
input = sys.stdin.readline

while True:
    n, m = input().split()
    n = int(n)

    if n == 0:
        break
    
    m = int(float(m)*100+0.5)

    cost = []
    calorie = []

    DP = [0 for j in range(m+1)]

    for i in range(n):
        c, p = input().split()
        p = int(float(p)*100+0.5)
        c = int(c)
        cost.append(p)
        calorie.append(c)

    for j in range(1, m+1):
        for i in range(n):
            if cost[i] <= j:
                DP[j] = max(DP[j], DP[j-cost[i]] + calorie[i])

    print(DP[m])


# 시간초과
"""
import sys
input = sys.stdin.readline

while True:
    n, m = input().split()
    n = int(n)

    if n == 0:
        break
    
    m = int(float(m)*100)

    cost = []
    calorie = []

    DP = [0 for j in range(m+1)]

    for i in range(n):
        c, p = input().split()
        p = int(float(p)*100)
        c = int(c)
        cost.append(p)
        calorie.append(c)

    for i in range(1,n+1):
        for c in range(1,(m//cost[i-1])+2):
            for j in range(1, m+1):
                if c*cost[i-1] <= j:
                    DP[j] = max(DP[j-1], DP[j-c*cost[i-1]] + c*calorie[i-1])

    print(DP[m])
"""
