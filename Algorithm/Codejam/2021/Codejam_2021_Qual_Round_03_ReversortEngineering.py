'''
2021 Codejam Qualification Round
03_Reversort Engineering

Sample Input
5
4 6
2 1
7 12
7 2
2 1000

Sample Output
Case #1: 4 2 1 3
Case #2: 1 2
Case #3: 7 6 5 4 3 2 1
Case #4: IMPOSSIBLE
Case #5: IMPOSSIBLE
'''

T = int(input())
for t in range(T):
    N, C = map(int, input().split())
    answer = list(map(str, range(1, N+1)))
    possible = N-1

    C -= possible
    turn = 0

    while possible >= 1 and C >= 0:
        if C < possible:
            possible = C
        C -= possible
        answer[turn//2:turn//2+possible+1] = reversed(answer[turn//2:turn//2+possible+1])
        if (C == 0): break
        possible -= 1
        turn += 1
    else:
        answer = 'IMPOSSIBLE'
        print(f"Case #{t+1}: {answer}")
        continue

    print(f"Case #{t+1}: {' '.join(answer)}")


'''
※ 01_Reversort 코드를 이용하여 찾은 반례
8 20 을 입력하여 얻은 배열인 [Case #1: 8 1 2 3 4 5 6 7] 를
01 코드에 넣으면 14가 나온다.


T = int(input())
for t in range(T):
    N, C = map(int, input().split())
    answer = list(map(str, range(1, N+1)))
    possible = N-1

    C -= possible
    turn = 0

    while possible >= 1 and C >= 0:
        if C < possible:
            possible = C
        C -= possible
        answer[turn:turn+possible+1] = reversed(answer[turn:turn+possible+1])
        if (C == 0): break
        possible -= 1
        turn += 1
    else:
        answer = 'IMPOSSIBLE'
        print(f"Case #{t+1}: {answer}")
        continue

    print(f"Case #{t+1}: {' '.join(answer)}")
'''


'''
# sample 만 맞고 test set 1 틀림
# 0 부터 계속 reverse하는 방식은 0 자리에 있는 애 위치가 바뀌면서
# cost가 추가로 더 생겨버림
# sample case로 걸러내지 못한 반례는 한 번만 뒤집는 경우만 예시로 나와서 그런 것으로 추정됨

T = int(input())
for t in range(T):
    N, C = map(int, input().split())
    answer = list(map(str, range(1, N+1)))
    possible = N-1

    C -= possible
    
    while possible >= 1 and C >= 0:
        if C < possible:
            possible = C
        C -= possible
        answer[0:possible+1] = reversed(answer[0:possible+1])
        if (C == 0): break
        possible -= 1
    else:
        answer = 'IMPOSSIBLE'
        print(f"Case #{t+1}: {answer}")
        continue

    print(f"Case #{t+1}: {' '.join(answer)}")
'''
