"""
14888 연산자 끼워넣기

1. 나눗셈 계산을 단순히 // 로 하면 틀림 (세번째 예제 답이 48로 나옴)
"나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때는 C++14의 기준을 따른다.
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다."

2. max, min 범위가 문제에 "출력" 부분에 설명이 되어있는데,
이걸 고려하지 않아서 틀렸습니다가 나옴
"""

def dfs(cur, depth, a, b, c, d):
    global N, _min, _max
    if depth == N:
        if cur > _max:
            _max = cur
        if cur < _min:
            _min = cur
        return
    if a > 0:
        dfs(cur+A[depth], depth+1, a-1, b, c, d)
    if b > 0:
        dfs(cur-A[depth], depth+1, a, b-1, c, d)
    if c > 0:
        dfs(cur*A[depth], depth+1, a, b, c-1, d)
    if d > 0:
        dfs(int(cur/A[depth]), depth+1, a, b, c, d-1)
        #dfs(cur//A[depth], depth+1, a, b, c, d-1)
    

_max = -100000000
_min = 1000000000
N = int(input())
A = list(map(int,input().split()))
a, b, c, d = map(int, input().split())
dfs(A[0], 1, a, b, c, d)
print(_max)
print(_min)
