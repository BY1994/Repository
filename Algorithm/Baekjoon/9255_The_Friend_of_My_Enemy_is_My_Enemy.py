"""
9255 The Friend of My Enemy is My Enemy

그래프 문제
직계 친구만 출력하기
"""


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    connect = [[0 for i in range(101)] for j in range(101)]
    for _ in range(m):
        p1, p2 = map(int, input().split())
        connect[p1][p2] = 1
        connect[p2][p1] = 1
    s = int(input())
    print(f"Data Set {tc}:")
    for i in range(1, n+1):
        if connect[s][i]:
            print(i, end=" ")
    print()
    print()
