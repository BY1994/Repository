"""
2021 Hackercup

B Traffic Control

output 이 잘리지 않게 idle shell 말고
cmd 창에서 실행하기

wait time은 1 ~ 1000 까지
1로 채우는 꼼수로 풀 건데,
A, B가 1000 보다 작거나 같다는 제한 조건이 있어서
다행히 더한 값이 1000 을 넘을 일은 없을 것 같다.
"""


import sys
#sys.stdin = open("traffic_control_input.txt")
#sys.stdout = open("21_R1_04_traffic_control_final_output.txt", "wt")


T = int(input())

for tc in range(1, T+1):
    n, m, a, b = map(int, input().split())
    array = [[1] * m for _ in range(n)] # 이 형식으로 쓸 때 n이랑 m 이 헷갈림
    temp = a - (n+m-1-1) # 경로 n+m-1 이고 시작점 위치 -1 (n*m 이라 착각함)
    if temp <= 0:
        print(f"Case #{tc}: Impossible")
        continue
    
    array[0][0] = temp

    temp = b - (n+m-1-1)
    if temp <= 0:
        print(f"Case #{tc}: Impossible")
        continue
    
    array[n-1][0] = temp

    print(f"Case #{tc}: Possible")
    for i in range(n):
        for j in range(m):
            print(array[i][j], end = ' ')
        print()
