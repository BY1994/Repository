""" 
2523 별찍기-13
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

최초작성 2019.03.12 PBY
"""

N = int(input())

for row in range(1, N+1):
    print('*'*row)

for row in range(N-1, 0, -1):
    print('*'*(row))

# visual studio는 실행시 ctrl + f5
