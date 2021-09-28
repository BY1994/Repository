"""
11811 번 데스스타

비트마스크 공부

# list() 로 안 감싸고 map 만 써도 된다.
"""

N = int(input())
for i in range(N):
    num = 0
    cond = list(map(int, input().split()))
    for j in cond:
        num |= j
    print(num, end=" ")
print()

