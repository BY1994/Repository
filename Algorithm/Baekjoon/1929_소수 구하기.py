"""
1929 소수 구하기

2019.04.10 PBY 최초작성
"""

# M 이상 N 이하의 소수를 모두 출력
check = [False] * 1000001
check[0] = True; check[1] = True

for number in range(2, 1000001):
    for cae in range(2, 1000000//number+1):
        check[number*cae] = True

M, N = map(int, input().split())
for i in range(M, N+1):
    if check[i] == False:
        print(i)
