"""
7510 고급 수학

피타고라스 정리
"""

for i in range(1, int(input())+1):
    print(f"Scenario #{i}:")
    numbers = list(map(int, input().split()))
    _max = 0
    _sum = 0
    for j in numbers:
        if _max < j:
            _max = j
        _sum += j*j
    print("yes" if _sum - _max*_max == _max*_max else "no")
    print()

# sort 를 하는 방법도 있음
# https://www.acmicpc.net/source/18194151
