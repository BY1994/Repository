# non-decreasing = 같거나 증가하거나
# 한번이라도 decreasing이 나오면 YES를 출력

# time limit
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for l in range(1, n):
        _max = max(a[:l])
        _min = min(a[l:])
        if _max > _min:
            print("YES")
            break
    else:
        print("NO")

# 틀린 부분 발견 prev 업데이트를 빼먹음
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prev = a[0]
    for i in range(1, n):
        if prev > a[i]:
            print("YES")
            break
        prev = a[i]
    else:
        print("NO")
"""
