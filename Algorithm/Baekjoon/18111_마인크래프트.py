"""
18111 마인크래프트

완전 탐색
solved.ac 의 Class 2 문제인데, 문제 풀이를 이해하는게 한참 걸렸다...

반례
https://www.acmicpc.net/board/view/84796
2 2 0
256 256
0 0
정답 768 128

내 코드의 틀렸던 점: 블럭 1개당 시간이 드는 거라서 곱해줘야한다는 걸 생각 못함
예제로는 블럭을 1개씩만 빼거나 더했기 때문에 이런 문제를 발견하지 못했다.
"""

N, M, B = map(int, input().split())
total = N*M
earth = []
for i in range(N):
    height = list(map(int, input().split()))
    earth.extend(height)
earth.sort(reverse=True)

min_time = 1000000000
ans = 0
for i in range(256, -1, -1):
    b = B
    time = 0
    for j in range(total):
        if earth[j] == i:
            continue
        if earth[j] > i:
            b += earth[j] - i
            time += 2 * (earth[j] - i)
        elif b >= (i - earth[j]):
            b -= i - earth[j]
            time += 1 * (i - earth[j])
        else:
            break
    else:
        if time < min_time:
            min_time = time
            ans = i

print(min_time, ans)

# 틀렸습니다
"""
N, M, B = map(int, input().split())
total = N*M
earth = []
for i in range(N):
    height = list(map(int, input().split()))
    earth.extend(height)
earth.sort(reverse=True)

min_time = 1000000000
ans = 0
for i in range(256, -1, -1):
    b = B
    time = 0
    for j in range(total):
        if earth[j] == i:
            continue
        if earth[j] > i:
            b += earth[j] - i
            time += 2
        elif b >= (i - earth[j]):
            b -= i - earth[j]
            time += 1
        else:
            break
    else:
        if time < min_time:
            min_time = time
            ans = i
    print(i, time)

print(min_time, ans)
"""
