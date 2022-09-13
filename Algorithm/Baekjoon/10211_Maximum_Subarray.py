"""
10211 Maximum Subarray

누적합을 만들고 브루트 포스로 풀 수 있는데,
그리디한 방식으로 가능한 듯해서 통과 완료함
"""

T = int(input())
for tc in range(T):
    N = int(input())
    arrays = list(map(int, input().split()))
    _max = -1000100
    cur = 0
    for value in arrays:
        cur += value
        _max = max(_max, cur)
        if cur < 0:
            cur = 0
    print(_max)
