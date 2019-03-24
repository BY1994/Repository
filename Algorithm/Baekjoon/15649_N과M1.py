"""
15649 N과 M 1

2019.03.24 PBY 최초작성
"""

def series(depth):
    global N, M
    if depth == M: # M-1로 하면 3 1 일 때 시작하자마자 끝남
        print(' '.join(map(str, Marray)))
        return

    for i in range(1, N+1):
        if i not in Marray:
            Marray[depth] = i
            series(depth+1)
            Marray[depth] = 0 # global 변수니까 0으로 안 바꿔주면 바뀐 상태로 계속 공유


N, M = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

Marray = [0 for _ in range(M)]
series(0)

    
