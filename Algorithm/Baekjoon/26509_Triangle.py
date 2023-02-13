"""
26509 Triangle

기하학, 피타고라스 정리
직사각형을 반으로 갈라서 나올 수 있는 삼각형인지 보는 것이므로
3개의 길이가 같아야하고 피타고라스 정리도 만족해야함
"""

for tc in range(int(input())):
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())

    _min1 = min(a1, min(b1, c1))
    _max1 = max(a1, max(b1, c1))
    _min2 = min(a2, min(b2, c2))
    _max2 = max(a2, max(b2, c2))

    if a1**2 + b1**2 + c1**2 - _max1**2 == _max1**2 and \
       a2**2 + b2**2 + c2**2 - _max2**2 == _max2**2:
        if _min1 == _min2 and _max1 == _max2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
