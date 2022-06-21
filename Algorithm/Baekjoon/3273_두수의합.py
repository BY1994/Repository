"""
3273 두 수의 합

투포인터

반례
https://www.acmicpc.net/board/view/70911
input:
6
2 19 41 45 55 58
64
ans:
1

문제 조건에 서로 다른 양의 정수란 조건 있음!
"""

# 모범 풀이
# https://www.acmicpc.net/source/29724739
"""
    int i = 0;                              // start
    int j = n - 1;                          // end
    while (i < j) {
        if (a[i] + a[j] == x) {
            ans++;
            i++;
        } else if (a[i] + a[j] > x) {
            j--;
        } else {
            i++;
        }
    }
"""

# 처음에 x 보다 큰 경우가 나오지 않을 때, 오른쪽 포인터가 끝까지 가질 않는다
# 통과
# 그러나 쓸데없이 복잡하게 풀었음. 숫자가 같은 경우가 있는 줄 알고...
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()
ans = 0

# init
start = 1
for i in range(1, n):
    cur = numbers[0] + numbers[i]
    if cur == x:
        ans += 1
    elif cur > x:
        break
    start = i

# find all
for a1 in range(1, n-1):
    for a2 in range(start, a1, -1):
        cur = numbers[a1] + numbers[a2]
        if cur == x:
            ans += 1
        elif cur < x:
            break
        start = a2

print(ans)

# a1 이 몇 개 같은 경우 있을 수 있을 듯
# a1, a2 가 없는 경우 에러 발생 가능? a1 1부터이므로, a2 는 2부터라서 아예 돌지 않음
# 틀렸습니다
"""
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()
ans = 0

# init
start = 1
for i in range(1, n):
    cur = numbers[0] + numbers[i]
    if cur == x:
        ans += 1
        start = i
    elif cur > x:
        start = i
        break

# find all
for a1 in range(1, n-1):
    for a2 in range(start, a1, -1):
        cur = numbers[a1] + numbers[a2]
        if cur == x:
            ans += 1
            start = a2
        elif cur < x:
            break

print(ans)
"""

# 틀렸습니다
"""
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()
ans = 0

# init
start = 1
for i in range(1, n):
    cur = numbers[0] + numbers[i]
    if cur == x:
        ans += 1
        start = i
    elif cur > x:
        start = i
        break

# find all
for a1 in range(1, n-1):
    for a2 in range(start, a1, -1):
        cur = numbers[a1] + numbers[a2]
        if cur == x:
            ans += 1
            start = a2
        elif cur < x:
            start = a2
            break

print(ans)
"""
