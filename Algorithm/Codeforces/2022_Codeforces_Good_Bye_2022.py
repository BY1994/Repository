"""
Codeforces Good Bye 2022 A번 문제
Editorial: https://codeforces.com/blog/entry/110754

A번 문제를 못 풀었는데, 문제 조건을 덜 읽은 것이었다.
j 번째 operation 은 무조건 b의 j 번째 값을 a 로 옮기는 것이었다.
나는 전체 결과를 최대화해야한다고 생각했는데, b 의 j 번째를 무조건 덮어쓰는 것이라
꼭 결과가 최대는 아닐 수도 있었다.
"""
# 만약 매번 sort 하는 것이 시간이 부족하다면 우선순위 큐로 관리해야할 것
for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()

    flag = 0
    for i in range(m):
        a[0] = b[i]
        a.sort()
    print(sum(a))

# Wrong Answer
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    flag = 0
    change = min(n, m)
    a_ind = 0
    b_ind = m-change
    for i in range(change):
        if b[b_ind] > a[a_ind]:
            flag = 1
            a[a_ind] = b[b_ind]
            b_ind += 1
        a_ind += 1
    if flag == 0 and m % 2 == 1:
        a[0] = b[-1]
    print(sum(a))
"""

# Wrong Answer
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    # m 개수 무시하고...
    # a 의 최소보다 b 의 최대가 크면 바꾸기
    # 그런데 하나도 안 바뀌는 건... m 이 홀수개면 불가능
    # m 이 홀수개인데 하나도 못 바꿨으면 마지막 한 개라도 바꿔야함
    flag = 0
    for i in range(min(n,m)):
        if b[i] >= a[i]:
            flag = 1
            a[i] = b[i]
    if flag == 0 and m % 2 == 1:
        a[0] = b[0]
    print(sum(a))
"""
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for s in range(m):
        _min = 10**9+10
        _ind = 0
        for i in range(n):
            if a[i] < _min:
                _min = a[i]
                _ind = i
        _max = 0
        _ind2 = 0
        for i in range(m):
            if b[i] > _max:
                _max = b[i]
                _ind2 = i
        a[_ind], b[_ind2] = b[_ind2], a[_ind]
    print(sum(a))
"""
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    change = min(n, m)
    ans = sum(b[-change:])
    if n - change:
        ans += sum(a[-(n-change):])
    print(ans)
"""
