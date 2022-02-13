"""
전체 길이가 3개면 가능/불가능 여부 판별 쉬움
1 [3] 1

전체 길이가 3개가 아니면 한 번이라도 2를 넘는 기둥이 있는지 확인
2를 넘어야 옮길 수 있고, 다른 홀수 위치로 옮길 수 있음

"""

def calc_op(n, a):
    ans = 0
    for i in range(1, n-1):
        if a[i] % 2 == 0:
            ans += a[i]//2
        else:
            ans += a[i]//2 + 1
    return ans

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 3:
        if a[1]%2 == 0:
            print(calc_op(n, a))
        else:
            print(-1)
    else:
        over_two = False
        for i in range(1, n-1):
            if a[i] >= 2:
                over_two = True
                break
        if over_two:
            print(calc_op(n, a))
        else:
            print(-1)
