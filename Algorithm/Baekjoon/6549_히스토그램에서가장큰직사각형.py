"""
6549 히스토그램에서 가장 큰 직사각형

stack

https://www.acmicpc.net/board/view/81172
반례
5 4 3 2 1 2
5 5 2 1 2 3
0

답
6
5

내 출력
4
5

https://www.acmicpc.net/board/view/79054
반례
12 3 2 3 4 5 4 3 2 3 1 1 1
0

정답
18

출력
16

분할 정복 풀이
https://velog.io/@whddn0221/%ED%9E%88%EC%8A%A4%ED%86%A0%EA%B7%B8%EB%9E%A8%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95
https://as-j.tistory.com/98
"""

stack = [0] * 100001

while True:
    high = list(map(int, input().split()))
    if high[0] == 0:
        break

    stack[0] = (high[1], 1)
    sp = 0
    ans = 0

    for i in range(2, high[0]+1):
        if stack[sp][0] <= high[i]:
            sp += 1
            stack[sp] = (high[i], i)
        else:
            ind = i
            while sp >= 0 and stack[sp][0] > high[i]:
                ind = stack[sp][1]
                ans = max(ans, (i - ind)*stack[sp][0])
                sp -= 1

            sp += 1
            stack[sp] = (high[i], ind)

    while sp >= 0:
        ans = max(ans, ((high[0]+1) - stack[sp][1])*stack[sp][0])
        sp -= 1
    
    print(ans)

# 틀렸습니다 -> 3 ... 2 3 일 때 2로 맨 뒤까지 커버가 안 됨
"""
stack = [0] * 100001

while True:
    high = list(map(int, input().split()))
    if high[0] == 0:
        break

    stack[0] = (high[1], 1)
    sp = 0
    ans = 0

    for i in range(2, high[0]+1):
        if stack[sp][0] <= high[i]:
            sp += 1
            stack[sp] = (high[i], i)
        else:
            while sp >= 0 and stack[sp][0] > high[i]:
                ans = max(ans, (i - stack[sp][1])*stack[sp][0])
                ans = max(ans, (i - stack[sp][1]+1)*high[i])
                sp -= 1

            sp += 1
            stack[sp] = (high[i], i)

    # for example 2
    while sp >= 0:
        ans = max(ans, ((high[0]+1) - stack[sp][1])*stack[sp][0])
        sp -= 1
    
    print(ans)
"""

# 틀렸습니다 -> 4 3 일 때 3 + 3 = 6 이 되는 경우가 고려 안 됨
"""
stack = [0] * 100001

while True:
    high = list(map(int, input().split()))
    if high[0] == 0:
        break

    stack[0] = (high[1], 1)
    sp = 0
    ans = 0

    for i in range(2, high[0]+1):
        if stack[sp][0] <= high[i]:
            sp += 1
            stack[sp] = (high[i], i)
        else:
            while sp >= 0 and stack[sp][0] > high[i]:
                ans = max(ans, (i - stack[sp][1])*stack[sp][0])
                sp -= 1

            sp += 1
            stack[sp] = (high[i], i)

    # for example 2
    while sp >= 0:
        ans = max(ans, ((high[0]+1) - stack[sp][1])*stack[sp][0])
        sp -= 1
    
    print(ans)
"""
